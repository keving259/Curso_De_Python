animales =  ['perro', 'gato', 'loro', 'cocodrilo']
numeros = [10, 62, 12, 70]

# Recorriendo la lista animales
'''
for animal in animales:
    print(f"Ahora la variable 'animal' es igual a: {animal}")
    

# Recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
'''


# Iterar dos listas al mismo tiempo (deben de tener la misma cantidad de elementos)
for numero, animal in zip(animales, numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")

'''
# Range
for num in range(5, 10): # Desde el 5 hasta antes del 10. Si solo se da un parámetro empieza en 0 hasta el número dado
    print(num)
'''

# Forma no óptima de recorrer una lista con su índice
for num in range(len(numeros)): # len cuenta el número de elementos en un objeto
    print(numeros[num])

# Forma correcta de recorrer una lista con su índice
for num in enumerate(numeros): # enumerate sirve para recorrer una colección y devuelve pares
    '''En cada iteración num es una tupla
    (0, 10) <- indice es num[0], y valor es num[1]
    (1, 62)
    (2, 12)
    (3, 70)
    '''
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

# Usando else
for numero in numeros:
    print(f"Ejecutando el último bucle, valor actual: {numero}")
    
else: # A la altra del for/else
    print("El bucle termino")


#todo lo anterior funciona exactamente igual para tuplas y conjuntos


