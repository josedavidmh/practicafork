# Lista global que almacenará las ventas
ventas = []

# Definición de una excepción personalizada
class VentaError(Exception):
    # Constructor de la excepción
    def __init__(self, mensaje):
        # Se llama al constructor de la clase padre Exception
        super().__init__(mensaje)


# Función para registrar una venta
def registrar_venta():
    try:
        # Solicita el ID de la venta al usuario
        id_venta = int(input("Ingrese ID de la venta: "))

        # Solicita el nombre del producto
        producto = input("Ingrese nombre del producto: ")

        # Solicita la cantidad vendida
        cantidad = int(input("Ingrese cantidad: "))

        # Solicita el precio unitario
        precio = float(input("Ingrese precio unitario: "))

        # Validación: cantidad no puede ser negativa
        if cantidad <= 0:
            # Se lanza excepción personalizada
            raise VentaError("La cantidad debe ser mayor a cero")

        # Validación: precio no puede ser negativo
        if precio <= 0:
            raise VentaError("El precio debe ser mayor a cero")

    except ValueError:
        # Captura errores de conversión (int o float)
        print("Error: Tipo de dato inválido")

    except VentaError as e:
        # Captura la excepción personalizada
        print(f"Error en la venta: {e}")

    else:
        # Se ejecuta si no ocurre ninguna excepción
        venta = {
            "id": id_venta,
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        }

        # Se agrega la venta a la lista
        ventas.append(venta)

        print("Venta registrada correctamente")

    finally:
        # Siempre se ejecuta, haya error o no
        print("Proceso de registro finalizado\n")