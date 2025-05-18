# This is a Google Cloud Function that uses FastAPI as the web framework.
from fastapi import FastAPI
from mangum import Mangum
from flask import Request, jsonify
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create a FastAPI app
app = FastAPI()

# Define a simple route
@app.get("/")
async def helloApi():
    return {"message": "Hello, World!"}

# Adapter for Google Cloud Functions
handler = Mangum(app)

def hello_world(request: Request):
    """
    Google Cloud Function entry point.
    Converts the incoming request to ASGI and processes it using FastAPI.
    """
    try:
        # Log the incoming request for debugging
        logger.debug("Incoming request: %s", request)
        
        # Convert the Google Cloud Function request to an ASGI-compatible request
        response = handler(request.environ, lambda status, headers: None)
        return response
    except Exception as e:
        # Log and handle errors gracefully
        logger.error("Error occurred: %s", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    from functions_framework import create_app
    app = create_app("hello_world")
    app.run(host="0.0.0.0", port=8080)

