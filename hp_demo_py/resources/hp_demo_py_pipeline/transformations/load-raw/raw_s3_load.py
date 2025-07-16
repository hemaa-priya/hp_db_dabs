from utilities.utils import read_from_s3_autoloader
from config.config import S3_PATHS, SCHEMA_LOC
import dlt

@dlt.table
def raw_orders():
    df = read_from_s3_autoloader(
        spark,
        s3_path=S3_PATHS["orders"],
        file_format="csv",
        schema_location=SCHEMA_LOC["orders"],
        extra_options={"header": "true"}
    )
    return df