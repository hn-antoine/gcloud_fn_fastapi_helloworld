from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum  # ⚠️ not needed in this context
import functions_framework
from werkzeug.wrappers import Request as WSGIRequest
from fastapi.middleware.wsgi import WSGIMiddleware

# Define FastAPI app
app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from FastAPI on GCF!"}

# Wrap FastAPI app with WSGI middleware
wrapped_app = WSGIMiddleware(app)

# Google Cloud Function entry point
@functions_framework.http
def helloApi(request: WSGIRequest):
    """Entrypoint for GCF"""
    return wrapped_app(request.environ, lambda status, headers: (status, headers))