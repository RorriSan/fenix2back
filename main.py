
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.json.ensure_ascii = False

cors = CORS(app, resources={"/api-fenix2/*": {"origins": "*"}})

# Importar las vistas
from componentes.vistasapi import *
from componentes.vistaweb import *

# Lo siguiente sólo en desarrollo, no en producción
if __name__ == '__main__':
    app.run()
    
