#creando funcion que suma numeros
def sumar_dos():
    # Iniciando un bucle infinito
    while True:
        # Pidiendo al usuario que ingrese dos números
        a = input("Número 1: ")
        b = input("Número 2: ")
        
        # Intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        except ValueError as e:
            # Si lanzó una excepción, pedirle que reingrese los números
            print("Te pedí un número salame, no te hagas el gracioso")
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print("No se puede dividir por cero")
            # Si todo salió bien, salir del bucle
        else: # Se puede usar else en un try-except. Solo se ejecuta si no hubo excepción
            break
        # Finally es opcional, se ejecuta sin importar si hubo excepción o no
        finally:
            print("Esto se ejecuta siempre")
        
    # Mostrando el resultado de la suma
    return resultado

print(sumar_dos())
