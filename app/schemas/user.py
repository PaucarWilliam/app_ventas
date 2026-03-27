from pydantic import BaseModel

class UserCreate(BaseModel):
    nombre: str
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    nombre: str
    email: str
    username: str

    class Config:
        orm_mode = True