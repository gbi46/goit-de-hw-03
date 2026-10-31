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
