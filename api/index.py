from main import app as flask_app

def handler(request):
    return flask_app(request.environ, start_response=lambda *args: None)
