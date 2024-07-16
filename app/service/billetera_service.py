from typing import List, Optional
from datetime import datetime
from app.models.cuenta import CuentaUsuario, Operacion


class BilleteraService:
    def __init__(self):
        self.cuentas = [
            CuentaUsuario(numero="21345", nombre="Arnaldo", saldo=200, contactos=["123", "456"]),
            CuentaUsuario(numero="123", nombre="Luisa", saldo=400, contactos=["456"]),
            CuentaUsuario(numero="456", nombre="Andrea", saldo=300, contactos=["21345"])
        ]

    def obtener_contactos(self, numero: str) -> List[CuentaUsuario]:
        cuenta = self._obtener_cuenta(numero)
        if not cuenta:
            return []
        return [self._obtener_cuenta(contacto) for contacto in cuenta.contactos if self._obtener_cuenta(contacto)]

    def realizar_pago(self, numero_origen: str, numero_destino: str, valor: float) -> bool:
        cuenta_origen = self._obtener_cuenta(numero_origen)
        cuenta_destino = self._obtener_cuenta(numero_destino)

        if not cuenta_origen or not cuenta_destino:
            return False

        if cuenta_origen.saldo < valor:
            return False

        cuenta_origen.saldo -= valor
        cuenta_destino.saldo += valor

        operacion = Operacion(
            tipo="Pago",
            monto=valor,
            numero_origen=numero_origen,
            numero_destino=numero_destino,
            fecha=datetime.now()
        )

        cuenta_origen.operaciones.append(operacion)
        cuenta_destino.operaciones.append(operacion)

        return True

    def obtener_historial(self, numero: str) -> Optional[CuentaUsuario]:
        return self._obtener_cuenta(numero)

    def _obtener_cuenta(self, numero: str) -> Optional[CuentaUsuario]:
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta
        return None