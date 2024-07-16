from fastapi import APIRouter, HTTPException
from app.service.billetera_service import BilleteraService
from app.schemas.cuenta import ContactoResponse, HistorialResponse, PagoResponse
from datetime import datetime

router = APIRouter()
billetera_service = BilleteraService()

@router.get("/contactos")
def obtener_contactos(minumero: str):
    contactos = billetera_service.obtener_contactos(minumero)
    return [ContactoResponse(numero=contacto.numero, nombre=contacto.nombre) for contacto in contactos]


@router.post("/pagar")
def realizar_pago(minumero: str, numerodestino: str, valor: float) -> PagoResponse:
    if billetera_service.realizar_pago(minumero, numerodestino, valor):
        return PagoResponse(mensaje=f"Realizado en {datetime.now().strftime('%d/%m/%Y')}")
    raise HTTPException(status_code=400, detail="No se pudo realizar el pago")

@router.get("/historial")
def obtener_historial(minumero: str) -> HistorialResponse:
    cuenta = billetera_service.obtener_historial(minumero)
    if not cuenta:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    
    operaciones = [f"{'Pago recibido' if op.numero_destino == minumero else 'Pago realizado'} "
                   f"de {op.monto} {'de' if op.numero_destino == minumero else 'a'} "
                   f"{billetera_service._obtener_cuenta(op.numero_origen).nombre if op.numero_destino == minumero else billetera_service._obtener_cuenta(op.numero_destino).nombre}"
                   for op in cuenta.operaciones]
    
    return HistorialResponse(saldo=cuenta.saldo, operaciones=operaciones)