# Vistas para la arquitectura API REST
from flask import jsonify
from flask import request

from main import app
from componentes.modelos import Cliente

@app.route("/api-fenix2/clientes", methods=['GET'])
def api_clientes():
    clientes = Cliente.obtener()
    datos = [cliente.__dict__ for cliente in clientes]
    
    return jsonify(datos)

