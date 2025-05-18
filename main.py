# This is a Google Cloud Function that uses FastAPI as the web framework.
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import functions_framework
from werkzeug.wrappers import Request as WSGIRequest

# Create a FastAPI app
app = FastAPI()

# Define a simple route
@app.get("/")
async def helloApi():
    return {"message": "Hello, World!"}

# Wrap the FastAPI app with WSGIMiddleware
wrapped_app = WSGIMiddleware(app)

@functions_framework.http
def hello_world(request: WSGIRequest):
    """
    Google Cloud Function entry point.
    Converts the incoming request to WSGI and processes it using FastAPI.
    """
    return wrapped_app(request.environ, lambda status, headers: None)

