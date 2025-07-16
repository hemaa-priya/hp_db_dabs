from utilities.api import fetch_api_data
import dlt
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.getActiveSession()
# Define the schema
schema = StructType([
    StructField("userId", IntegerType(), True),
    StructField("id", IntegerType(), True),
    StructField("title", StringType(), True),
    StructField("body", StringType(), True)
])

# Fetch the data and create DataFrame with schema
data = [fetch_api_data(endpoint="https://jsonplaceholder.typicode.com/posts/1")]
df = spark.createDataFrame(data, schema=schema)

@dlt.table(name="hp_sf_test.hp_schema.api_streaming_table")
def api_streaming_table():
    return df
