from pyspark.sql import DataFrame
def read_from_s3_autoloader(
    spark,
    s3_path: str,
    file_format: str = "csv",
    schema_location: str = "/mnt/checkpoints/schema",
    extra_options: dict = None
) -> DataFrame:
    """
    Reusable function to read from S3 using Auto Loader.
    """
    options = {
        "cloudFiles.format": file_format,
        "cloudFiles.schemaLocation": schema_location
    }
    if extra_options:
        options.update(extra_options)
    return (
        spark.readStream.format("cloudFiles")
        .options(**options)
        .load(s3_path)
    )
