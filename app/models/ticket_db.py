from sqlalchemy import Column, Integer, String
from app.database import Base

class TicketDB(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String)
    descripcion = Column(String)
    estado = Column(String)