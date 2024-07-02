# Vistas según patrón MVT (Model View Template)
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from main import app
from componentes.modelos import Cliente

@app.route('/')
def inicio():
    return render_template('./inicio.html')