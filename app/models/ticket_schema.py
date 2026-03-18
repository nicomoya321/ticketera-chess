from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    titulo: str = Field(..., min_length=3, max_length=100)
    descripcion: str = Field(..., min_length=5)
    estado: str = Field(..., pattern="^(abierto|cerrado|en progreso)$")