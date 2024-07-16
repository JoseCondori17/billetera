from datetime import date

class CuentaUsuario:
    def crear_cuenta(self, nombre: str, numero: str, saldo: float):
        self.nombre = nombre
        self.numero = numero
        self.saldo = saldo
        self.numeros_contacto = []
        self.historial = []

    def historialOperaciones(self):
        return self.historial

    def transferir(self, destino, valor: float) -> bool:
        if destino.numero in self.numeros_contacto and self.saldo >= valor:
            operacion = Operacion.crear_operacion(self, destino, valor, date.today())
            self.saldo -= valor
            destino.saldo += valor
            self.historial.append(operacion)
            destino.historial.append(operacion)
            return True
        return False

    def agregarContacto(self, contacto):
        self.numeros_contacto.append(contacto.numero)
    
    def listarContacto(self):
        print("Contactos de ", self.nombre)
        for contacto in self.numeros_contacto:
            print(contacto)

    def mostrarHistorial(self):
        print(f"Saldo actual de {self.nombre} ({self.numero}): {self.saldo}")
        print("Historial de operaciones:")
        for operacion in self.historial:
            tipo = "Envío" if operacion.origen == self else "Recepción"
            otro_usuario = operacion.destino if tipo == "Envío" else operacion.origen
            print(f"{tipo} - {otro_usuario.nombre} ({otro_usuario.numero}), Monto: {operacion.valor}, Fecha: {operacion.fecha}")


class Operacion:
    @classmethod
    def crear_operacion(cls, origen, destino, valor: float, fecha: date):
        operacion = cls()
        operacion.origen = origen
        operacion.destino = destino
        operacion.valor = valor
        operacion.fecha = fecha
        return operacion

'''
# Ejemplo de uso
cuenta1 = CuentaUsuario()
cuenta1.crear_cuenta("Natali", "957351428", 1000.0)

cuenta2 = CuentaUsuario()
cuenta2.crear_cuenta("Eduardo", "908749413", 1500.0)

# Agregar contacto
cuenta1.agregarContacto(cuenta2)

# Listar contactos
cuenta1.listarContacto()
print()

# Transferir dinero
resultado = cuenta1.transferir(cuenta2, 200.0)
print("¿Transferencia exitosa?: ", resultado)
resultado = cuenta1.transferir(cuenta2, 200.0)
print("¿Transferencia exitosa?: ", resultado)
print()

# Mostrar historial de operaciones
cuenta1.mostrarHistorial()
print()
cuenta2.mostrarHistorial()
'''