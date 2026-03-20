from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import tickets
from app.routes import auth  

app = FastAPI()  # ← esto faltaba antes del middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(tickets.router, prefix="/tickets", tags=["tickets"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])  # ← registrar auth
