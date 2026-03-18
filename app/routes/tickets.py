from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal  # pyright: ignore[reportMissingImports]
from app.models.ticket_db import TicketDB  # pyright: ignore[reportMissingImports]
from app.models.ticket_schema import TicketCreate # pyright: ignore[reportMissingImports]
from app.auth import get_current_user  # pyright: ignore[reportMissingImports]

router = APIRouter()

# GET
@router.get("/tickets")
def get_tickets(user: str = Depends(get_current_user)): 
    db: Session = SessionLocal()
    tickets = db.query(TicketDB).all()
    db.close()
    return tickets

# POST (PRO)
@router.post("/tickets")
def create_ticket(ticket: TicketCreate, user: str = Depends(get_current_user)): # type: ignore
    db: Session = SessionLocal()

    new_ticket = TicketDB(
        titulo=ticket.titulo,
        descripcion=ticket.descripcion,
        estado=ticket.estado
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    db.close()

    return {"mensaje": f"Ticket creado por {user}", "ticket": new_ticket}