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

def process_df(df, records_limit):
    cleaned_df = df.dropna()
    cleaned_df.show(records_limit)

users_df = spark.read.csv(str(data_dir / 'users.csv'), header=True, inferSchema=True)
purchases_df = spark.read.csv(str(data_dir / 'purchases.csv'), header=True, inferSchema=True)
products_df = spark.read.csv(str(data_dir / 'products.csv'), header=True, inferSchema=True)

if __name__ == "__main__":
    if sys.argv[1:] == ["show"]:
        show_data(
            users=users_df,
            purchases=purchases_df,
            products=products_df,
        )
