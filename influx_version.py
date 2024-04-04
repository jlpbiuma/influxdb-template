from influxdb_client import InfluxDBClient

# For InfluxDB 2.x
url = "http://localhost:8086"
token = "YourTokenHere"
org = "yourOrg"
bucket = "yourBucket"

client = InfluxDBClient(url=url, token=token, org=org)
print(client)