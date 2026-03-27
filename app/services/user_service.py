from sqlalchemy.orm import Session
from app.db.models.users import User

def create_user(db: Session, user_data):
    new_user = User(
        nombre = user_data.nombre,
        email= user_data.email,
        username = user_data.username,
        password_hash= user_data.password # Luego se hashea esto
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user