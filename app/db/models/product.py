from sqlalchemy import Column, Integer, String, Numeric, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.session import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'


    id = Column(Integer, primary_key=True, autoincrement= True)
    _nombre = Column('nombre', String(150), nullable=False)
    descripcion = Column(Text)
    _precio = Column('precio', Numeric(10, 2), nullable=False)
    marca = Column(String(150), nullable=False)
    stock_actual = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, nullable=False, default=0)
    
     #server_default=func.now() indica 
    creado_en = Column(TIMESTAMP, server_default=func.now())

    @property
    def nombre(self):
        return self._nombre.title() if self._nombre else None
   
    @nombre.setter
    def nombre(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value

    @property
    def precio(self):
        return float(self._precio) if self._precio else 0.0

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = value

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self._nombre}', precio={self._precio})>"
    
    