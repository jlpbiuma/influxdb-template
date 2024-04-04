import influxdb_client
import os
import time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import load_dotenv
from faker import Faker
import random

# Load environment variables from .env file
load_dotenv()

TOKEN = os.environ.get("INFLUXDB_TOKEN")
ORG = "my-org"
URL = "http://localhost:8086"
BUCKET = "my-new-bucket"

client = influxdb_client.InfluxDBClient(url=URL, token=TOKEN, org=ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Generate synthetic device information
def generate_device_info():
    fake = Faker()
    device_id = fake.uuid4()
    mac_address = fake.mac_address()
    ip_address = fake.ipv4()
    location = fake.city()
    name = fake.word()
    return {'device_id': device_id, 'mac_address': mac_address, 'ip_address': ip_address, 'location': location, 'name': name}

# Generate synthetic sensor data
def generate_sensor_data(device_id):
    humidity = random.uniform(0, 100)
    temperature = random.uniform(-20, 50)
    co_concentration = random.uniform(0, 1000)
    return {'device_id': device_id, 'humidity': humidity, 'temperature': temperature, 'co_concentration': co_concentration}

for value in range(5):
    device_info = generate_device_info()
    print(device_info)
    sensor_data = generate_sensor_data(device_info['device_id'])
    print(sensor_data)
    device_point = (
        Point("devices")
        .tag("location", device_info['location'])
        .field("mac_address", device_info['mac_address'])
        .field("ip_address", device_info['ip_address'])
        .field("name", device_info['name'])
    )
    
    sensor_point = (
        Point("sensors")
        # .tag("location", device_info['location'])
        .field("humidity", sensor_data['humidity'])
        .field("temperature", sensor_data['temperature'])
        .field("co_concentration", sensor_data['co_concentration'])
    )

    write_api.write(bucket=BUCKET, org=ORG, record=device_point)
    write_api.write(bucket=BUCKET, org=ORG, record=sensor_point)
    
    time.sleep(1) # separate points by 1 second
