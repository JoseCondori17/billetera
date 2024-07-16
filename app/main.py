from fastapi import FastAPI
from app.api.billetera import router as billetera_router

app = FastAPI()
app.include_router(billetera_router, prefix="/billetera")