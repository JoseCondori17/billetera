import pytest
from app.service.billetera_service import BilleteraService

@pytest.fixture
def billetera_service():
    return BilleteraService()

# Casos de existo

def test_realizar_pago_exitoso(billetera_service):
    """
    @Caso de prueba: Realizar un pago exitoso entre dos cuentas existentes.
    @Lo que se espera: Que el pago se realice correctamente y los saldos se actualicen.
    """
    resultado = billetera_service.realizar_pago("21345", "123", 100)
    assert resultado == True
    cuenta_origen = billetera_service._obtener_cuenta("21345")
    cuenta_destino = billetera_service._obtener_cuenta("123")
    assert cuenta_origen.saldo == 100
    assert cuenta_destino.saldo == 500

def test_obtener_contactos_existentes(billetera_service):
    """
    @Caso de prueba: Obtener contactos de una cuenta existente.
    @Lo que se espera: Que se devuelva la lista correcta de contactos.
    """
    contactos = billetera_service.obtener_contactos("21345")
    assert len(contactos) == 2
    assert contactos[0].numero == "123"
    assert contactos[1].numero == "456"

# Casos de error

def test_realizar_pago_saldo_insuficiente(billetera_service):
    """
    @Caso de prueba: Intentar realizar un pago con saldo insuficiente.
    @Lo que se espera: El pago falle y los saldos no se modifiquen.
    """
    resultado = billetera_service.realizar_pago("21345", "123", 300)
    assert resultado == False
    cuenta_origen = billetera_service._obtener_cuenta("21345")
    cuenta_destino = billetera_service._obtener_cuenta("123")
    assert cuenta_origen.saldo == 200
    assert cuenta_destino.saldo == 400

def test_realizar_pago_cuenta_inexistente(billetera_service):
    """
    @Caso de prueba: Intentar realizar un pago a una cuenta que no existe
    @Lo que se espera: El pago falle y no se realicen cambios.
    """
    resultado = billetera_service.realizar_pago("21345", "999", 100)
    assert resultado == False
    cuenta_origen = billetera_service._obtener_cuenta("21345")
    assert cuenta_origen.saldo == 200

def test_obtener_historial_cuenta_inexistente(billetera_service):
    """
    @Caso de prueba: Intentar obtener el historial de una cuenta inexistente.
    @Lo que se espera: Se devuelva None si la cuenta no existe.
    """
    historial = billetera_service.obtener_historial("999")
    assert historial is None