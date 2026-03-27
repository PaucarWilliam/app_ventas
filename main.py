from fastapi import FastAPI
from app.api.routes import product

app = FastAPI()
app.include_router(product.router)