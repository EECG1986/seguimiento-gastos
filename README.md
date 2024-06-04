# Aplicación de Seguimiento de Gastos

Esta es una aplicación de terminal para seguir tus gastos personales. Puedes registrar ingresos y gastos, listar transacciones y generar un balance financiero.

## Características

- **Agregar Transacción**: Registra ingresos y gastos.
- **Listar Transacciones**: Muestra las transacciones ordenadas por fecha.
- **Balance**: Muestra el total de ingresos, gastos y capacidad de ahorro.
- **Guardar Datos**: Guarda las transacciones en un archivo.
- **Cargar Datos**: Carga las transacciones desde un archivo.

## Requisitos

- Python 3.x

## Instalación

1. Clona el repositorio o descarga los archivos:

   ```bash
   git clone https://github.com/EECG1986/seguimiento-gastos.git
'''

2. Navega al directorio del proyecto:
    '''cd seguimiento-gastos
'''

## Uso

1. Ejecuta el script principal 'seguimiento_gastos.py' para iniciar la aplicación:
   '''python seguimiento_gastos.py
'''
## Menú de Opciones

1. Agregar Transacción
2. Listar Transacciones
3. Calcular Balance
4. Guardar Datos
5. Cargar Datos
6. Salir

## Ejemplo de Uso

1. Agregar Transacción:
'''Seleccione una opción: 1
Ingrese el monto: 1000
Ingrese la fecha (YYYY-MM-DD): 2024-06-03
Ingrese la descripción: Sueldo
Ingrese el tipo (ingreso/gasto): ingreso
Transacción agregada: Sueldo, ingreso, 1000, 2024-06-03
'''
2. Listar Transacciones:
'''Seleccione una opción: 2
2024-06-03 - Sueldo - ingreso - 1000.0
'''
3. Cargar Datos:
'''Seleccione una opción: 5
Datos cargados correctamente.
luego seleccione opción: 2
'''

--- Menú de Seguimiento de Gastos ---
1. Agregar Transacción
2. Listar Transacciones
3. Calcular Balance
4. Guardar Datos
5. Cargar Datos
6. Salir

4. Seleccione una opción: 2
2024-04-30 - salario basico mensual - ingreso - 2000000.0
2024-05-01 - canasta familiar - gasto - 600000.0
2024-05-10 - gastos hormiga - gasto - 200000.0
2024-05-15 - pago proveedores servicios publicos  - gasto - 300000.0
2024-05-29 - pago proveedor alojamiento - gasto - 700000.0


# Aplicación de Seguimiento de Gastos

class Transaccion:
Clase que representa una transacción financiera.

Atributos: monto (float): El monto de la transacción. fecha (datetime): La fecha de la transacción. descripcion (str): Una descripción de la transacción. tipo (str): El tipo de transacción ('ingreso' o 'gasto').

Transaccion(monto: float, fecha: str, descripcion: str, tipo: str)
Inicializa una nueva transacción.

Args: monto (float): El monto de la transacción. fecha (str): La fecha de la transacción en formato 'YYYY-MM-DD'. descripcion (str): Una descripción de la transacción. tipo (str): El tipo de transacción ('ingreso' o 'gasto').

monto
fecha
descripcion
tipo
class Finanzas:
Clase que maneja las finanzas personales.

Atributos: transacciones (List[Transaccion]): Lista de transacciones registradas.

Finanzas()
Inicializa una instancia de Finanzas con una lista vacía de transacciones.

transacciones: List[seguimiento_gastos.seguimiento-gastos.Transaccion]
def agregar_transaccion(self, monto: float, fecha: str, descripcion: str, tipo: str):
Agrega una nueva transacción a la lista de transacciones.

Args: monto (float): El monto de la transacción. fecha (str): La fecha de la transacción en formato 'YYYY-MM-DD'. descripcion (str): Una descripción de la transacción. tipo (str): El tipo de transacción ('ingreso' o 'gasto').

def listar_transacciones(self):
Muestra todas las transacciones ordenadas por fecha.

def calcular_balance(self):
Calcula y muestra el balance financiero actual.

Muestra el total de ingresos, el total de gastos y la capacidad de ahorro (ingresos - gastos).

def guardar_datos(self):
Guarda las transacciones en un archivo 'datos_financieros.pkl' utilizando el módulo pickle.

def cargar_datos(self):
Carga las transacciones desde un archivo 'datos_financieros.pkl' utilizando el módulo pickle.

Si el archivo no existe, inicializa las transacciones en un estado vacío.

def mostrar_menu():
Muestra el menú de opciones al usuario.

def main():
Función principal que ejecuta el flujo de la aplicación.

Permite al usuario interactuar con el sistema de finanzas personales mediante un menú de opciones.