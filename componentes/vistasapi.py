# Vistas para la arquitectura API REST
from flask import jsonify
from flask import request

from main import app
from componentes.modelos import Cliente

@app.route("/api-fenix2/", methods=['GET'])
def api_clientes():
    clientes = Cliente.obtener_todos()
    # datos = [c.__dict__ for c in clientes]
    return jsonify(clientes)

@app.route("/api-fenix2/registro", methods=['POST'] )
def registrar():
 # if request.method == 'POST':
 # print(request.json)     
# @app.route("/api-fenix2/clientes", methods=['POST'])
# def crear_cliente():

    if request.method == 'POST':
        datos = request.json["datos"]
        cta_nueva = Cliente(
            datos['nombre'],
            datos['apellido'],
            datos['telefono'],
            datos['correo'],
            datos['usuario'],
            datos['password'],
        )
        
        respuesta = {}
        
        try:
            cta_nueva.guardar_db()
            respuesta['mensaje'] = 'Cuenta creada con éxito!'
            respuesta['status'] = 200
            
            print('estoyaca')
            
        except Exception as e:
            respuesta['mensaje'] = 'No se puedo crear la cuenta!'
            respuesta['status'] = 409
            
    else:
        respuesta['mensaje'] = 'No se recibieron datos.'
        respuesta['status'] = 204    

    # return  jsonify({"mensaje": "llego algo"}) 
    return jsonify(respuesta)
