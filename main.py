from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Flask in Cloud Function!'

# Entry point for Google Cloud Functions
# Delegate to the WSGI app using functions-framework compatibility
def hello_world(request):
    return app(request.environ, start_response_wrapper)

def start_response_wrapper(status, response_headers, exc_info=None):
    # Collect status and headers to return a proper response object
    from werkzeug.wrappers import Response
    return lambda body: Response(body, status=status, headers=dict(response_headers))
