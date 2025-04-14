import os
import shutil
from datetime import datetime
from flask import Blueprint, render_template, current_app, send_file
from src.app.utils import generate_cv, clean_old_tmp_files

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/download_cv", endpoint="download_cv_file")
def download_cv():
    # Definir carpeta temporal y asegurar su existencia
    tmp_folder = os.path.join(current_app.root_path, "tmp")
    os.makedirs(tmp_folder, exist_ok=True)

    # Limpiar archivos antiguos (más de 1 hora)
    clean_old_tmp_files(tmp_folder, max_age_seconds=3600)

    # Generar el CV
    docx_path, _ = generate_cv()
    docx_path = os.path.abspath(docx_path)

    if not os.path.exists(docx_path):
        return f"El archivo no se encuentra en la ubicación esperada: {docx_path}", 404

    # Crear un nombre único para el archivo temporal
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_tmp_path = os.path.join(tmp_folder, f"cv_{timestamp}.docx")

    # Mover el archivo generado a la carpeta temporal
    try:
        shutil.move(docx_path, unique_tmp_path)
    except Exception as e:
        return f"Error al mover el archivo: {e}", 500

    # Enviar el archivo al cliente
    return send_file(
        unique_tmp_path,
        as_attachment=True,
        download_name="cv.docx",
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


@main.route("/politica-de-privacidad")
def privacy_policy():
    return render_template("privacy_policy.html")


@main.route("/terminos-de-uso")
def terms_of_use():
    return render_template("terms_of_use.html")


@main.app_errorhandler(404)
def pagina_nofound(error):
    return render_template("404.html"), 404