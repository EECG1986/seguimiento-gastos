import pickle
from datetime import datetime
from typing import List

class Transaccion:
    """
    Clase que representa una transacción financiera.

    Atributos:
        monto (float): El monto de la transacción.
        fecha (datetime): La fecha de la transacción.
        descripcion (str): Una descripción de la transacción.
        tipo (str): El tipo de transacción ('ingreso' o 'gasto').
    """

    def __init__(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """
        Inicializa una nueva transacción.

        Args:
            monto (float): El monto de la transacción.
            fecha (str): La fecha de la transacción en formato 'YYYY-MM-DD'.
            descripcion (str): Una descripción de la transacción.
            tipo (str): El tipo de transacción ('ingreso' o 'gasto').
        """
        self.monto = monto
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d')
        self.descripcion = descripcion
        self.tipo = tipo

class Finanzas:
    """
    Clase que maneja las finanzas personales.

    Atributos:
        transacciones (List[Transaccion]): Lista de transacciones registradas.
    """

    def __init__(self):
        """Inicializa una instancia de Finanzas con una lista vacía de transacciones."""
        self.transacciones: List[Transaccion] = []

    def agregar_transaccion(self, monto: float, fecha: str, descripcion: str, tipo: str):
        """
        Agrega una nueva transacción a la lista de transacciones.

        Args:
            monto (float): El monto de la transacción.
            fecha (str): La fecha de la transacción en formato 'YYYY-MM-DD'.
            descripcion (str): Una descripción de la transacción.
            tipo (str): El tipo de transacción ('ingreso' o 'gasto').
        """
        nueva_transaccion = Transaccion(monto, fecha, descripcion, tipo)
        self.transacciones.append(nueva_transaccion)
        print(f"Transacción agregada: {descripcion}, {tipo}, {monto}, {fecha}")

    def listar_transacciones(self):
        """Muestra todas las transacciones ordenadas por fecha."""
        self.transacciones.sort(key=lambda x: x.fecha)
        for t in self.transacciones:
            print(f"{t.fecha.date()} - {t.descripcion} - {t.tipo} - {t.monto}")

    def calcular_balance(self):
        """
        Calcula y muestra el balance financiero actual.

        Muestra el total de ingresos, el total de gastos y la capacidad de ahorro (ingresos - gastos).
        """
        total_ingresos = sum(t.monto for t in self.transacciones if t.tipo == 'ingreso')
        total_gastos = sum(t.monto for t in self.transacciones if t.tipo == 'gasto')
        capacidad_ahorro = total_ingresos - total_gastos
        print(f"Total Ingresos: {total_ingresos}")
        print(f"Total Gastos: {total_gastos}")
        print(f"Capacidad de Ahorro: {capacidad_ahorro}")

    def guardar_datos(self):
        """
        Guarda las transacciones en un archivo 'datos_financieros.pkl' utilizando el módulo pickle.
        """
        with open('datos_financieros.pkl', 'wb') as archivo:
            pickle.dump(self.transacciones, archivo)
        print("Datos guardados correctamente.")

    def cargar_datos(self):
        """
        Carga las transacciones desde un archivo 'datos_financieros.pkl' utilizando el módulo pickle.

        Si el archivo no existe, inicializa las transacciones en un estado vacío.
        """
        try:
            with open('datos_financieros.pkl', 'rb') as archivo:
                self.transacciones = pickle.load(archivo)
            print("Datos cargados correctamente.")
        except FileNotFoundError:
            print("No se encontró el archivo de datos. Se inicializa en un estado vacío.")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Menú de Seguimiento de Gastos ---")
    print("1. Agregar Transacción")
    print("2. Listar Transacciones")
    print("3. Calcular Balance")
    print("4. Guardar Datos")
    print("5. Cargar Datos")
    print("6. Salir")

def main():
    """
    Función principal que ejecuta el flujo de la aplicación.

    Permite al usuario interactuar con el sistema de finanzas personales mediante un menú de opciones.
    """
    finanzas = Finanzas()
    finanzas.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto: "))
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            descripcion = input("Ingrese la descripción: ")
            tipo = input("Ingrese el tipo (ingreso/gasto): ")
            finanzas.agregar_transaccion(monto, fecha, descripcion, tipo)
        elif opcion == "2":
            finanzas.listar_transacciones()
        elif opcion == "3":
            finanzas.calcular_balance()
        elif opcion == "4":
            finanzas.guardar_datos()
        elif opcion == "5":
            finanzas.cargar_datos()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
