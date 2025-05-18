# This is a Google Cloud Function that uses FastAPI as the web framework.
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
import functions_framework
from werkzeug.wrappers import Request as WSGIRequest

# FastAPI app
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on GCF!"}

# Wrap with WSGI middleware
wrapped_app = WSGIMiddleware(app)

# Cloud Function HTTP entry point
@functions_framework.http
def helloApi(request: WSGIRequest):
    """Entrypoint for Google Cloud Function"""
    response_body = []
    status_headers = {}

    def start_response(status, headers):
        status_headers["status"] = status
        status_headers["headers"] = headers
        return response_body.append

    result = wrapped_app(request.environ, start_response)
    response_body = b"".join(response_body + list(result))
    return (response_body, int(status_headers["status"].split()[0]), status_headers["headers"])

# Run locally using functions-framework or directly with `python main.py`
if __name__ == "__main__":
    print("Running locally on http://localhost:8080")
    run_simple("0.0.0.0", 8080, wrapped_app)

    