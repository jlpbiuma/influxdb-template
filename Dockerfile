# Use the official InfluxDB image
FROM influxdb:latest

# Copy influxdb configuration file
COPY influxdb.conf /etc/influxdb/influxdb.conf

# Set environment variables
ENV DOCKER_INFLUXDB_INIT_MODE=setup \
    DOCKER_INFLUXDB_INIT_USERNAME=my-user \
    DOCKER_INFLUXDB_INIT_PASSWORD=my-password \
    DOCKER_INFLUXDB_INIT_ORG=my-org \
    DOCKER_INFLUXDB_INIT_BUCKET=my-bucket \
    DOCKER_INFLUXDB_INIT_RETENTION=1w \
    DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=my-super-secret-auth-token

# Set up initial databases and users
COPY init_script.txt /docker-entrypoint-initdb.d/init_script.txt

# Expose port 8086
EXPOSE 8086

# Define volume for data
VOLUME /var/lib/influxdb2

# Define volume for configuration
VOLUME /etc/influxdb2
