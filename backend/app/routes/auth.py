from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.core.security import (
    hash_password, verify_password,
    create_access_token, get_current_user
)
from app.models.user import User

router = APIRouter()

class RegisterSchema(BaseModel):
    email: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(data: RegisterSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(email=data.email, password_hash=hash_password(data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered", "user_id": new_user.id}

@router.post("/login")
def login_user(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return {"id": current_user.id, "email": current_user.email}
