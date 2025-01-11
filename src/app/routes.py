import os
from flask import render_template, current_app, send_file
from flask import Blueprint
from src.app.utils import generate_cv

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route('/download_cv', endpoint='download_cv_file')
def download_cv():
    docx_path, _ = generate_cv()

    docx_path = os.path.abspath(docx_path)

    if not os.path.exists(docx_path):
        return f"El archivo no se encuentra en la ubicación esperada: {docx_path}", 404

    tmp_folder = os.path.join(current_app.root_path, 'tmp')  
    if not os.path.exists(tmp_folder):
        os.makedirs(tmp_folder)

    tmp_path = os.path.join(tmp_folder, 'Orlibet_Dun_CV.docx')

    try:
        os.rename(docx_path, tmp_path)
    except FileNotFoundError as e:
        return f"Error al mover el archivo: {e}", 500

    if not os.path.exists(tmp_path):
        return f"El archivo no se encuentra en la carpeta temporal: {tmp_path}", 500

    return send_file(tmp_path, as_attachment=True)

@main.route('/politica-de-privacidad')
def privacy_policy():
    return render_template('privacy_policy.html')

@main.route('/terminos-de-uso')
def terms_of_use():
    return render_template('terms_of_use.html')