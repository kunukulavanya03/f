from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.database import engine, Base
from app.models import User
from app.schemas import UserCreate, User, UserUpdate
from app.authentication import authenticate_user, get_user

router = APIRouter(tags=['users'])

@router.get("/api/health")
def read_health():
    return {"status": "ok", "timestamp": "now"}

@router.get("/api/users")
def read_users():
    users = session.query(User).all()
    return {"users": users}

@router.post("/api/users")
def create_user(user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    session.add(new_user)
    session.commit()
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}

@router.get("/api/users/{id}")
def read_user(id: int):
    user = session.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

@router.put("/api/users/{id}")
def update_user(id: int, user: UserUpdate):
    user_to_update = session.query(User).filter(User.id == id).first()
    if not user_to_update:
        raise HTTPException(status_code=404, detail="User not found")
    user_to_update.name = user.name
    user_to_update.email = user.email
    session.commit()
    return {"id": user_to_update.id, "name": user_to_update.name, "email": user_to_update.email}

@router.delete("/api/users/{id}")
def delete_user(id: int):
    user_to_delete = session.query(User).filter(User.id == id).first()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user_to_delete)
    session.commit()
    return {"message": "User deleted"}