# Se importa la lista ventas desde el módulo registro_ventas
from registro_ventas import ventas


# Excepción personalizada para consultas
class ConsultaError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


# Función para mostrar todas las ventas
def mostrar_ventas():
    try:
        # Validar si la lista está vacía
        if len(ventas) == 0:
            # Lanzar excepción personalizada
            raise ConsultaError("No hay ventas registradas")

    except ConsultaError as e:
        # Captura la excepción personalizada
        print(f"Error: {e}")

    else:
        # Si hay ventas, se muestran
        print("\nListado de ventas:")
        for venta in ventas:
            # Se imprime cada venta
            print(venta)

    finally:
        # Siempre se ejecuta
        print("Consulta finalizada\n")


# Función para buscar una venta por ID
def buscar_venta():
    try:
        # Solicita el ID a buscar
        id_busqueda = int(input("Ingrese ID de la venta a buscar: "))

        # Variable para indicar si se encontró
        encontrada = False

        # Recorre la lista de ventas
        for venta in ventas:
            # Verifica si coincide el ID
            if venta["id"] == id_busqueda:
                print("Venta encontrada:", venta)
                encontrada = True

        # Si no se encontró, lanzar excepción
        if not encontrada:
            raise ConsultaError("Venta no encontrada")

    except ValueError:
        # Error si el ID no es número
        print("Error: ID inválido")

    except ConsultaError as e:
        print(f"Error: {e}")

    else:
        print("Búsqueda realizada correctamente")

    finally:
        print("Proceso de búsqueda finalizado\n")