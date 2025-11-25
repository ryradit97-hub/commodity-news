from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Vercel!", "status": "working"}

@app.get("/api")  
def api_root():
    return {"message": "API endpoint working", "status": "ok"}

# For Vercel
from mangum import Mangum
handler = Mangum(app)