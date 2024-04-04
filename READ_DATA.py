from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Connect to InfluxDB
client = InfluxDBClient(url="http://localhost:8086", token="my-super-secret-auth-token", org="my-org")

def query_devices():
    # Query to retrieve device information
    query = 'from(bucket: "my-new-bucket") |> range(start: -1d) |> filter(fn: (r) => r._measurement == "devices")'
    result = client.query_api().query(query, org="my-org")
    print("Devices:")
    for table in result:
        for record in table.records:
            device_id = record.values.get("device_id")
            mac_address = record.values.get("mac_address")
            ip_address = record.values.get("ip_address")
            location = record.values.get("location")
            name = record.values.get("name")
            print(f"Device ID: {device_id}, MAC Address: {mac_address}, IP Address: {ip_address}, Location: {location}, Name: {name}")

def query_sensors():
    # Query to retrieve sensor data
    query = 'from(bucket: "my-new-bucket") |> range(start: -1d) |> filter(fn: (r) => r._measurement == "sensors")'
    result = client.query_api().query(query, org="my-org")
    print("\nSensor Data:")
    for table in result:
        for record in table.records:
            device_id = record.values.get("device_id")
            humidity = record.values.get("humidity")
            temperature = record.values.get("temperature")
            co_concentration = record.values.get("co_concentration")
            print(f"Device ID: {device_id}, Humidity: {humidity}, Temperature: {temperature}, CO Concentration: {co_concentration}")

if __name__ == "__main__":
    query_devices()
    query_sensors()
