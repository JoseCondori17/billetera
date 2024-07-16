from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Operacion(BaseModel):
    tipo: str
    monto: float
    numero_origen: str
    numero_destino: str
    fecha: datetime


class CuentaUsuario(BaseModel):
    numero: str
    nombre: str
    saldo: float
    contactos: List[str]
    operaciones: List[Operacion] = []