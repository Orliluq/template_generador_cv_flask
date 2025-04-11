from main import app as flask_app
from werkzeug.wrappers import Response

def handler(request):
    response = Response.from_app(flask_app, request.environ)
    return response
