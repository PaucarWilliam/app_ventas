from sqlalchemy import Column, Integer, String, Numeric, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.session import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'proveedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    _nombre = Column('nombre', String(150), nullable=False)
    _contacto = Column('contacto', String(150), nullable=False)
    telefono = Column(String(50), nullable=False)
    creado_en = Column(TIMESTAMP, server_default=func.now())

    @property
    def nombre(self):
        return self._nombre.title() if self._nombre else None
    
    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío.")
        self.nombre = value
    
    @property
    def contacto(self):
        return self._contacto.title() if self._contacto else None
    
    @contacto.setter
    def contacto(self, value):
        if not value:
            raise ValueError("El contacto no puede estar vacío.")
        self.nombre = value
    
    def __repr__(self):
        return f"<Proveedor(id={self.id}, nombre='{self._nombre}', contacto={self.contacto})>"