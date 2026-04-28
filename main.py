"""
EJERCICIO: Sistema básico de gestión de ventas (Trabajo colaborativo)

Descripción:
Se debe desarrollar un sistema en Python dividido en tres módulos que permita:
1. Registrar ventas
2. Consultar ventas registradas
3. Ejecutar el sistema desde un módulo principal (main)

Condiciones:
- NO se permite usar bases de datos.
- Se debe trabajar con listas internas.
- Cada módulo debe ser desarrollado por un integrante del equipo.
- Se debe implementar manejo robusto de excepciones:
    * try/except
    * try/except/else
    * try/except/finally
    * Excepciones personalizadas

Estructura del proyecto:
- main.py → menú principal
- registro_ventas.py → lógica para registrar ventas
- consulta_ventas.py → lógica para consultar ventas

Datos de cada venta:
- ID de venta
- Producto
- Cantidad
- Precio unitario

El sistema debe validar:
- Que los datos sean correctos
- Que no haya valores negativos
- Que los tipos de datos sean adecuados

Objetivo:
Comprender la modularidad, el trabajo colaborativo con GitHub
y el manejo de excepciones en Python.
"""




# Importa funciones de los otros módulos
from registro_ventas import registrar_venta
from consulta_ventas import mostrar_ventas, buscar_venta


# Función principal del sistema
def menu():
    while True:
        try:
            # Mostrar menú
            print("=== SISTEMA DE VENTAS ===")
            print("1. Registrar venta")
            print("2. Mostrar ventas")
            print("3. Buscar venta")
            print("4. Salir")

            # Solicita opción al usuario
            opcion = int(input("Seleccione una opción: "))

            # Validación de opción
            if opcion < 1 or opcion > 4:
                raise ValueError("Opción fuera de rango")

        except ValueError as e:
            # Manejo de error
            print(f"Error: {e}")

        else:
            # Flujo normal
            if opcion == 1:
                registrar_venta()

            elif opcion == 2:
                mostrar_ventas()

            elif opcion == 3:
                buscar_venta()

            elif opcion == 4:
                print("Saliendo del sistema...")
                break

        finally:
            # Siempre se ejecuta
            print("Regresando al menú...\n")


# Punto de entrada del programa
if __name__ == "__main__":
    # Llama al menú
    menu()