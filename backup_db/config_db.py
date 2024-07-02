import mysql.connector

config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'fenix2'
}

config_prod = {
    'user': 'rodrisan',
    'password': 'Fenix1234$',
    'host': 'rodrisan.mysql.pythonanywhere-services.com',
    'database': 'rodrisan$fenix2'
}

conexion = mysql.connector.connect(**config_dev)