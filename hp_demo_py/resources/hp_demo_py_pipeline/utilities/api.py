import requests
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf
import json

@udf(returnType=StringType())
def fetch_api_data(endpoint, params=None, headers=None):
    response = requests.get(endpoint, params=params, headers=headers)
    response.raise_for_status()
    return json.dumps(response.json())