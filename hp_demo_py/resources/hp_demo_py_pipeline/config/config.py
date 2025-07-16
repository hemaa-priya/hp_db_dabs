TABLES = {
    "raw_orders": "hp_sf_test.hp_schema.raw_orders",
    "silver_orders": "hp_sf_test.default.raw_orders_silver"
}
API_ENDPOINTS = {
    "orders": "https://jsonplaceholder.typicode.com/posts/1"
}
S3_PATHS = {
    "orders": "s3://hp-root-s3/"
}
SCHEMA_LOC = {
    "orders": "/mnt/checkpoints/schema"
}