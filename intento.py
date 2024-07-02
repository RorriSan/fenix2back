import mysql.connector

conexion = mysql.connector.connect(user = 'root',
                                   password = '',
                                   host = '127.0.0.1',
                                   database = 'fenix2')


cursor = conexion.cursor()

consulta = " SELECT * FROM clientes;"

cursor.execute(consulta)

datos = cursor.fetchall()
print(datos)

conexion.close()



