from sqlalchemy.orm import Session
from .models import AdminUser, Message
from .auth import hash_password
from .shema_pydantic import CreateUser, GetMessage

def create_user(db : Session, data:CreateUser) :
    user = AdminUser(
        username = data.username,
        hashed_password = hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_message(db : Session, data : GetMessage) :
    message = Message(
        full_name = data.full_name,
        email = data.email,
        sujet = data.sujet,
        message = data.message,
        created_at = data.created_at
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

