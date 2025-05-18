from fastapi import FastAPI
import os

# Create a FastAPI app
app = FastAPI()

# Define a simple route
@app.get('/')
async def hello_world():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=int(os.environ.get('PORT', 8081)))
