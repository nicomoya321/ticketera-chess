from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_db import UserDB
from app.models.user_schema import UserCreate, UserLogin
from app.security import hash_password, verify_password
from app.auth import create_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db: Session = SessionLocal()

    existing = db.query(UserDB).filter(UserDB.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    new_user = UserDB(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"mensaje": "Usuario creado"}

@router.post("/login")
def login(user: UserLogin):
    db: Session = SessionLocal()

    db_user = db.query(UserDB).filter(UserDB.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_token({"sub": user.username})

    db.close()

    return {"access_token": token}