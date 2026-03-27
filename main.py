from fastapi import FastAPI
from app.api.routes import product
from app.api.routes import user
from app.api.routes import supplier

app = FastAPI()
app.include_router(product.router)
app.include_router(user.router)
app.include_router(supplier.router)

