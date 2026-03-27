from pydantic import BaseModel

class SupplierSchema(BaseModel):
    nombre: str
    contacto: str
    telefono: str
    creado_en: str

