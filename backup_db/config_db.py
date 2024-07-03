import mysql.connector

config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'fenix2'
}

config_prod = {
    'user': 'Diego11',
    'password': 'Fenix1234$',
    'host': 'Diego11.mysql.pythonanywhere-services.com',
    'database': 'Diego11$default2'
}

conexion = mysql.connector.connect(**config_dev)