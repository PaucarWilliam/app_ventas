from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db 
from app.services import supplier_service
from app.schemas.supplier import SupplierSchema

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.get("/", response_model=List[SupplierSchema])
def listar_productos(db: Session = Depends(get_db)):
    return supplier_service.get_supplier(db)

@router.post("/", response_model=SupplierSchema)
def registrar_producto(supplier: SupplierSchema, db: Session = Depends(get_db)):
    return supplier_service.create_supplier(db=db, supplier_data=supplier.model_dump())