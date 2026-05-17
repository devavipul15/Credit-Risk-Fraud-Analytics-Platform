from fastapi import FastAPI
from app.api.fraud_routes import router as fraud_router

app = FastAPI(title="Financial AI Intelligence System")

app.include_router(fraud_router)

@app.get("/")
def home():
    return {"message": "Financial AI Intelligence System Running"}