from fastapi import HTTPException
from sqlalchemy.orm.session import Session

from .hashing import Hash
from .models import User
from routers.schemas import UserBase

hash = Hash()

def create_user(db:Session, request: UserBase):
    new_user = User(
        username=request.username,
        email=request.email,
        password= hash.bcrypt(request.password),

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db:Session, username:str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")
    return user

