#!/bin/sh

# Activar el entorno virtual
. venv/Scripts/activate

# Establecer el archivo principal de Flask
export FLASK_APP=main.py

# Asignar el puerto (por defecto 5000 si no está definido)
export PORT=${PORT:-5000}

# Ejecutar el servidor Flask
python -m flask run --debug --port=$PORT
