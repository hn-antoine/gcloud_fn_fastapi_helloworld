from flask import Flask, jsonify, request
import functions_framework

# Create a Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    """
    A simple Flask route that returns a Hello, World! message.
    """
    return jsonify({"message": "Hello, World!"})

@functions_framework.http
def hello_world(request):
    """
    Google Cloud Function entry point.
    Handles HTTP requests and returns a Hello, World! message.
    """
    return app(request.environ, lambda status, headers: None)
