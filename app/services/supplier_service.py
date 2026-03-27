from sqlalchemy.orm import Session
from app.db.models.supplier import Supplier

def get_supplier(db: Session):
    return db.query(Supplier).all()

def create_supplier(db: Session, supplier_data: dict):
    new_supplier = Supplier(
        _nombre = supplier_data.get("nombre"),
        _contacto = supplier_data.get("contacto"),
        telefono = supplier_data.get("telefono"),
    )

    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier
