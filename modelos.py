import componentes.config_db as config_db

class Cliente:
    # Atributos de clase
    tabla = 'clientes'
    campos = ('nombre', 'apellido', 'telefono', 'mail', 'usuario', 'contraseña')
    conexion = config_db.conexion
    
    # Método constructor
    def __init__(self, nombre, apellido, telefono, mail, usuario, contraseña):
        # Atributo de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail = mail
        self.usuario = usuario
        self.contraseña = contraseña
        
        
    def guardar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        columns = ", ".join(self.campos)
        placeholders = ", ".join(["%s"] * len(self.campos))
        consulta = f"INSERT INTO {self.tabla} ({columns}) VALUES ({placeholders})"
        datos = (self.nombre, self.apellido, self.telefono, self.mail, self.usuario, self.contraseña)
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

        

    
    
    