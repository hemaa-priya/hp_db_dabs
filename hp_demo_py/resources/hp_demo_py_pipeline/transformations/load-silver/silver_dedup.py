import dlt
def create_latest_snapshot(table_name: str, bronze_schema: str, silver_schema: str, keys: list | None = None):
    source_table_name = f"{bronze_schema}.{table_name}"
    latest_view_name = spark.conf.get("latest_view_name")
    silver_latest_table_name = f"hp_sf_test.default.{table_name}_silver"

    if keys is None:
        keys = ["id"]

    @dlt.view(
        name=latest_view_name,
        comment=f"Latest snapshot view for {table_name}"
    )
    @dlt.expect("not_null_keys", "id IS NOT NULL AND updated_timestamp IS NOT NULL")
    def create_latest_view():
        query = f"""
          SELECT *
          FROM {source_table_name}
          WHERE updated_timestamp = (
              SELECT MAX(updated_timestamp)
              FROM {source_table_name}
          )
          """
        return spark.sql(query)

    dlt.create_streaming_table(silver_latest_table_name)
    dlt.create_auto_cdc_from_snapshot_flow(
        target = silver_latest_table_name,
        source = latest_view_name,
        keys = keys,
        stored_as_scd_type = 1
    )

create_latest_snapshot(spark.conf.get("raw_tbl_name"), "hp_schema", "default")
