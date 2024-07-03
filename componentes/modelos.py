import backup_db.config_db as config_db
import mysql.connector
from componentes.dml import Tabla
from backup_db.config_db import conexion as con
from auxiliares.cifrado import encriptar

class Cliente(Tabla):
    
    tabla = 'clientes'
    conexion = con
    campos = ('id', 'nombre', 'apellido', 'telefono', 'mail', 'usuario', 'password')
    
    # Curso(tema, inicio, cierre, docente, cupo)
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)


class Cliente:
    # Atributos de clase
    tabla = 'clientes'
    campos = ('nombre', 'apellido', 'telefono', 'mail', 'usuario', 'password')
    conexion = config_db.conexion
    
    # Método constructor
    def __init__(self, nombre, apellido, telefono, mail, usuario, password):
        # Atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.usuario = usuario
        self.password = password
        
        
    def guardar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        columns = ", ".join(self.campos)
        placeholders = ", ".join(["%s"] * len(self.campos))
        consulta = f"INSERT INTO {self.tabla} ({columns}) VALUES ({placeholders})"
        datos = (self.nombre, self.apellido, self.telefono, self.mail, self.usuario, self.password)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        self.conexion.close()
    
    @classmethod
    def obtener_todos(cls):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla}"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cls.conexion.close()
        return datos 

        

    
    
    