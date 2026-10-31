from pyspark.sql import functions as F

def purchases_sum(purchases_df, products_df):
    category_totals = (
        purchases_df
        .join(products_df, on="product_id", how="inner")
        .groupBy("category")
        .agg(
            F.round(
                F.sum(F.col("quantity") * F.col("price")),
                2,
            ).alias("total_amount")
        )
        .orderBy(F.desc("total_amount"))
    )

    category_totals.show(truncate=False)


def purchases_share_by_users_age_range(purchases_df, products_df, users_df, age_from, age_to):
    """Return category shares of total spending for an inclusive age range."""
    category_totals = purchases_by_users_age_range(
        purchases_df, products_df, users_df, age_from, age_to
    )
    total_spending = category_totals.agg(
        F.sum("total_amount").alias("total_spending")
    )

    return (
        category_totals
        .crossJoin(total_spending)
        .withColumn(
            "share_percent",
            F.when(
                F.col("total_spending") != 0,
                F.round(F.col("total_amount") / F.col("total_spending") * 100, 2),
            ).otherwise(F.lit(0.0))
        )
        .drop("total_spending")
        .orderBy(F.desc("total_amount"))
    )

def purchases_by_users_age_range(purchases_df, products_df, users_df, age_from, age_to):
    """Return purchase totals by product category for an inclusive age range."""
    users_in_range = users_df.filter(
        F.col("age").between(age_from, age_to)
    ).select("user_id")

    return (
        purchases_df
        .join(users_in_range, on="user_id", how="inner")
        .join(products_df, on="product_id", how="inner")
        .groupBy("category")
        .agg(
            F.round(
                F.sum(F.col("quantity") * F.col("price")),
                2,
            ).alias("total_amount")
        )
        .orderBy(F.desc("total_amount"))
    )
