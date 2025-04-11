import os
from flask import render_template, current_app, send_file
from flask import Blueprint
from src.app.utils import generate_cv
from datetime import datetime

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route('/download_cv', endpoint='download_cv_file')
def download_cv():
    # Generar el archivo CV y obtener la ruta
    docx_path, _ = generate_cv()

    # Asegurarse de que la ruta es absoluta
    docx_path = os.path.abspath(docx_path)

    if not os.path.exists(docx_path):
        return f"El archivo no se encuentra en la ubicación esperada: {docx_path}", 404

    # Definir la carpeta temporal donde se guardará el archivo
    tmp_folder = os.path.join(current_app.root_path, 'tmp')  
    if not os.path.exists(tmp_folder):
        os.makedirs(tmp_folder)

    # Crear un nombre único para el archivo usando la fecha y hora
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_tmp_path = os.path.join(tmp_folder, f"cv_{timestamp}.docx")

    # Intentar mover el archivo a la carpeta temporal
    try:
        os.rename(docx_path, unique_tmp_path)
    except FileNotFoundError as e:
        return f"Error al mover el archivo: {e}", 500

    # Verificar si el archivo se movió correctamente
    if not os.path.exists(unique_tmp_path):
        return f"El archivo no se encuentra en la carpeta temporal: {unique_tmp_path}", 500

    # Enviar el archivo al cliente
    return send_file(unique_tmp_path, as_attachment=True)

@main.route('/politica-de-privacidad')
def privacy_policy():
    return render_template('privacy_policy.html')

@main.route('/terminos-de-uso')
def terms_of_use():
    return render_template('terms_of_use.html')
