import sys
import os
import time
from flask import request

# Agregar el directorio src al path para poder importar create_app
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

# Importar la función create_app desde src/app.py
from src.app import create_app

# Crear la instancia de la aplicación Flask
app = create_app()


@app.before_request
def start_timer():
    request.start_time = time.time()


@app.after_request
def log_response(response):
    duration = time.time() - request.start_time
    print(
        f"{request.method} {request.path} → {response.status_code} in {duration:.4f}s"
    )
    return response


if __name__ == "__main__":
    # Ejecuta la aplicación en modo debug local, pero en producción Render debe usar Gunicorn
    app.run(debug=True, host="0.0.0.0", port=5000)
