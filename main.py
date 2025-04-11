from src.app import create_app
from flask import Flask, request
import time

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_response(response):
    duration = time.time() - request.start_time
    print(f"{request.method} {request.path} → {response.status_code} in {duration:.4f}s")
    return response