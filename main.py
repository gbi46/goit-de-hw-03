from lib.purchases import purchases_by_users_age_range, purchases_sum
from lib.show_data import show_data
from pathlib import Path
from pyspark.sql import SparkSession

import os
import sys

os.environ["SPARK_CONF_DIR"] = str(
    Path(__file__).resolve().parent / "conf"
)

# Create spark session
spark = SparkSession.builder.appName('MySparkSandbox').getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

path = Path()

data_dir = path.parent / 'data'

def process_df(df):
    return df.dropna()

users_df = spark.read.csv(str(data_dir / 'users.csv'), header=True, inferSchema=True)
users_df = process_df(users_df)

purchases_df = spark.read.csv(str(data_dir / 'purchases.csv'), header=True, inferSchema=True)
purchases_df = process_df(purchases_df)

products_df = spark.read.csv(str(data_dir / 'products.csv'), header=True, inferSchema=True)
products_df = process_df(products_df)

if __name__ == "__main__":
    if sys.argv[1:] == ["show"]:
        show_data(
            users=users_df,
            purchases=purchases_df,
            products=products_df,
        )
    elif sys.argv[1:] == ["sum"]:
        purchases_sum(purchases_df, products_df)
    elif sys.argv[1:] == ["sum-by-age"]:
        purchases_by_users_age_range(
            purchases_df,
            products_df,
            users_df,
            18,
            25
        ).show(truncate=False)
