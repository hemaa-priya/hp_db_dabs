import dlt
from pyspark.sql.functions import col, current_timestamp, expr
from config.config import TABLES

@dlt.table
def gold_recent_active_users():
    df = dlt.read(TABLES["silver_orders"])
    return (
        df.filter(
            (col("gender") == "Female") &
            (col("updated_timestamp") <= expr("current_timestamp() - INTERVAL 100 DAYS"))
        )
    )

