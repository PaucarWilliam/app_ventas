from sqlalchemy.orm import Session
from app.db.models.product import Producto

def get_products(db: Session):
    """Retorna la lista de objetos Producto desde la BD"""
    return db.query(Producto).all()

def create_product(db: Session, product_data: dict):
    new_product = Producto(
        _nombre=product_data.get("nombre"), # Mapea 'nombre' a '_nombre'
        descripcion=product_data.get("descripcion"),
        _precio=product_data.get("precio"),
        marca=product_data.get("marca"),
        stock_actual=product_data.get("stock_actual"),
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product