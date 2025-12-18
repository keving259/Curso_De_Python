#falto el profe y los pibes van a armar la clase.

# Función para obtener el asistente y el profesor según la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    # Creando la lista con los compañeros
    compañeros = []
    
    # Ejecutando for para pedir información de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad) # Compañero va a ser una tupla con nombre y edad
        
        # Agregando la información a la lista
        compañeros.append(compañero)
        
    # Ordenándolos de menor a mayor según su edad
    compañeros.sort(key=lambda x:x[1]) # Ordena de menor a mayor los compañeros por key, que es el elemento con índice 1 en la tupla (la edad)
    # Lo que se tiene es una lista [(nombre, edad), (nombre, edad), (nombre, edad)]
    asistente = compañeros[0][0] # Se accede al emeneto [0] de la lista, y después se selecciona el elemento [0] de la tupla (el nombre)
    profesor = compañeros[-1][0] # Se accede al último elemento (que tiene el valor edad más alto) y luego se accede al elemento [0] (el nombre)
    
    return asistente, profesor


'''Compañeros [x] devuelve una tupla con (nombre, edad) y después accedemos al nombre para definir al asistente y el profesor'''
asistente, profesor = obtener_compañeros(5)

print(f"El profesor es {profesor}, y su asistente es {asistente}")
