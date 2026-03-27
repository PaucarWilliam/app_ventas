from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.db.session import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    username = Column(String(100), nullable=False)
    password_hash = Column(Text, nullable=False)
    creado_en = Column(TIMESTAMP, server_default=func.now())  # pylint: disable=not-callable