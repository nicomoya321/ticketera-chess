# app/database.py
import os
os.environ["PYTHONIOENCODING"] = "utf-8"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator

# SQLite temporal ← no necesita instalación
DATABASE_URL = "sqlite:///./tickets.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()