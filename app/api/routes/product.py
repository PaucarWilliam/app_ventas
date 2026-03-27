from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db 
from app.services import product_service
from app.schemas.product import ProductSchema

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=List[ProductSchema])
def listar_productos(db: Session = Depends(get_db)):
    return product_service.get_products(db)

@router.post("/", response_model=ProductSchema)
def registrar_producto(producto: ProductSchema, db: Session = Depends(get_db)):
    return product_service.create_product(db=db, product_data=producto.model_dump())