# Plantilla Docker - InfluxDB - Python

## Docker

1. Mirar la configuración del Dockerfile para conocer las configuraciones de la base de datos
2. Ejecutar el siguiente comando para construir la imagen

```bash
docker build -t influxdb_custom .
```

3. Ejecutar este otro comando para inicializar el contenedor

```bash
docker run -d --name influxdb_custom -p 8086:8086 influxdb_custom
```

## InfluxDB

1. Entrar en la siguiente [url](http://localhost:8086) para trabajar con el gestor de influxdb
2. Entrar en el tutorial de Python par trabajar con el cliente de ese lenguaje
3. Copiar el token que se muestra en el step 3
4. Generar un nuevo archivo llamado .env
5. Pegar el token de la siguiente forma

```bash
INFLUXDB_TOKEN='AQUI VA EL TOKEN ENTERO ENTRE LAS COMILLAS'
```

6. Guardar el archivo .env

## Python

1. Ejecutar el siguiente comando para inicializar el virtualenv

```bash
python -m venv .venv
```

2. Ejecutar el siguiente comando para instalar las dependencias del proyecto

```bash
pip install -r requirements.txt
```

3. Ejecutar el script CREATE_DATA para escribir datos en los buckets de influxdb (pendiente de corregir ya que se escriben null)
4. Ejecutar el script READ_DATA para leer los datos de un cierto bucket
