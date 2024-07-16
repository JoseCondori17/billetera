from pydantic import BaseModel
from typing import List

class ContactoResponse(BaseModel):
    numero: str
    nombre: str

class HistorialResponse(BaseModel):
    saldo: float
    operaciones: List[str]

class PagoResponse(BaseModel):
    mensaje: str