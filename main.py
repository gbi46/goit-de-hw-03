from pathlib import Path
from pyspark.sql import SparkSession

# Create spark session
spark = SparkSession.builder.appName('MySparkSandbox').getOrCreate()

print(spark)

path = Path()

data_dir = path.parent / 'data'


