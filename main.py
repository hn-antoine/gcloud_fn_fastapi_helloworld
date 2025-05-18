from fastapi import FastAPI, Request
from mangum import Mangum

# Create a FastAPI app
app = FastAPI()

# Define a simple route
@app.get('/')
async def hello_world():
    return {"message": "Hello, FastAPI!"}

# Adapter for Google Cloud Functions
handler = Mangum(app)

def helloApi(request: Request):
    """
    Google Cloud Function entry point.
    Converts the incoming request to ASGI and processes it using FastAPI.
    """
    return handler(request)