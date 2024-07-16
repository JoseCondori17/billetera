
# Examen final - Billetera

Integrantes:
- Cecilia Natali Pilco Padilla
- Jose Eduardo Condori Palomino

La evaluacion cuenta con la implementacion de la API con FastAPI se ha estructurado la carpeta en:

- api
- models
- schema
- service
- test
- main.py 

Para ejecutar el programa primero tiene que instalar todas las dependencias utilizadas y de preferencias cree un entorno virtual para no tener errores de versiones o de incompatilidad

fastapi dev main.py}

Para ejecutar los casos de prueba

cd app
pytest .\test\test_billetera_service.py

Pregunta 3
## Cambios en el Código

Para soportar el valor máximo de 200 soles a transferir por día, se realizaron los siguientes cambios:

1. *Agregar un atributo a la clase CuentaUsuario:*
   - Se agregó un atributo de tipo diccionario que almacena la fecha y el monto total de transferencias por día.

2. *Modificar el método transferir en la clase CuentaUsuario:*
   - Se añadió la lógica para verificar el monto actual de transferencia diaria y asegurar que la sumatoria con el nuevo monto no exceda los 200 soles.
   - Si la transferencia es exitosa, se modifica el valor del monto en el diccionario. Si la transferencia falla, se muestra un mensaje de error.

## Nuevos Casos de Prueba

1. *Transferencia de monto mayor a 200 soles:*
   - Intentar realizar una transferencia única que exceda el límite de 200 soles y verificar que la transferencia falle.

2. *Flujo de transferencias cuya sumatoria exceda los 200 soles:*
   - Realizar múltiples transferencias en el mismo día cuya sumatoria exceda los 200 soles y verificar que la última transferencia falle.

## Errores de Funcionalidad con Casos de Prueba Existentes

Sí, los casos de prueba existentes junto a los nuevos casos de prueba garantizan:
- Que no se exceda el monto de transferencia diario.
- El correcto funcionamiento de las transferencias de fondos entre contactos.
- La verificación de saldo.
- El historial de operaciones.
