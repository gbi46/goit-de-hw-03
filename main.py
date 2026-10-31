from pathlib import Path
from pyspark.sql import SparkSession

# Create spark session
spark = SparkSession.builder.appName('MySparkSandbox').getOrCreate()

path = Path()

data_dir = path.parent / 'data'

users_df = spark.read.csv(str(data_dir / 'users.csv'), header=True, inferSchema=True)
purchases_df = spark.read.csv(str(data_dir / 'purchases.csv'), header=True, inferSchema=True)
products_df = spark.read.csv(str(data_dir / 'products.csv'), header=True, inferSchema=True)
