from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configura las rutas, extensiones y otros aspectos del app aquí
    # Ejemplo:
    # app.config.from_object('config.Config')

    return app