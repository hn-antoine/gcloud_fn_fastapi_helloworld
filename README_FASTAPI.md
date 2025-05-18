# gcloud_fn_fastapi_helloworld

This project demonstrates a simple "Hello, World!" Google Cloud Function using FastAPI.

## Step-by-Step Instructions

### 1. Prerequisites
- Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
- Ensure you have a Google Cloud project set up. Note the project ID.
- Enable the **Cloud Functions API** for your project.
- Install Python 3.9 or later (if not already installed).
- Install the required Python packages:
  ```bash
  pip install fastapi mangum
  ```

### 2. Clone the Repository
```bash
git clone <repository-url>
cd gcloud_fn_fastapi_helloworld
```

### 3. Write the Function Code
The `main.py` file should contain the following code:
```python
from fastapi import FastAPI, Request
from mangum import Mangum

# Create a FastAPI app
app = FastAPI()

# Define a simple route
@app.get('/')
async def hello_world():
    return {"message": "Hello, World!"}

# Adapter for Google Cloud Functions
handler = Mangum(app)

def helloApi(request: Request):
    """
    Google Cloud Function entry point.
    Converts the incoming request to ASGI and processes it using FastAPI.
    """
    return handler(request)
```

### 4. Deploy the Function

#### 4.1. Deploy Using Google CLI
Run the following command to deploy the function:
```bash
gcloud functions deploy helloApi \
    --runtime python310 \
    --trigger-http \
    --allow-unauthenticated \
    --project <your-project-id>
```
Replace `<your-project-id>` with your actual Google Cloud project ID.

#### 4.2. Deploy Using Google Cloud Console
Alternatively, you can deploy the function using the Google Cloud Console:

1. Navigate to the [Cloud Functions page](https://console.cloud.google.com/functions) in the Google Cloud Console.
2. Click **Create Function**.
3. Enter a name for your function (e.g., `helloApi`).
4. Select **HTTP** as the trigger type and check the box for **Allow unauthenticated invocations**.
5. Under the **Source** section, upload the `main.py` file.
6. Specify the entry point as `helloApi`.
7. Choose the runtime as `Python 3.10`.
8. Click **Deploy**.

Once deployed, the function's URL will be displayed. Use this URL to test your function as described in Step 5.

### 5. Test the Function
After deployment, note the URL provided in the output. Test the function by visiting the URL in your browser or using `curl`:
```bash
curl <function-url>
```
Replace `<function-url>` with the URL of your deployed function.

### 6. Clean Up
To avoid incurring charges, delete the deployed function when no longer needed:
```bash
gcloud functions delete helloApi --project <your-project-id>
```