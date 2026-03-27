from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    marca: Optional[str] = None
    stock_actual: int

    model_config = {
            "from_attributes": True
    }