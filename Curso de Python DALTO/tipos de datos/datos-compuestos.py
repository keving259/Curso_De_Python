### DATOS COMPUESTOS

## LISTAS Y TUPLAS
# Los datos compuesto contienen datos simples u otros datos complejos, pero se pueden agrupar

#creando una lista (se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]
# creando una tupla (no se puede modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

print(lista[1])
print(tupla[1])

#print(lista[1]) # Imprime el elemento 1 (empezando a contar desde 0 de izquierda a derecha) de lista

lista[3] = "Maquinola" # Ahora el elemento con índice 3 es "Maquinola"
print(lista[3])

# Con las tuplas da error:
#tupla[3] = "Maquinola" 



## CONJUNTOS (SETS)

''' 
El orden de los elementos no representan nada, por lo que pueden cambiar de posición, pero no se pueden modificar. Tampoco se pueden repetir valores, a diferencia de las listas y las tuplas
Se crean con llaves
'''
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

# Da error
#conjunto[1] = "Pedrín"

# Se puede sobreescribir

conjunto = {"xdxdxd"}
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85}

# NO se puede acceder por el índice
#print(conjunto[1]) <- No puede acceder al elemento

# No se pueden repetir valores
#conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.85, "Soy Dalto"}



## DICCIONARIOS

'''
Es literlamente un JSON. Se almacenan claves y valores (key, value)
'''

diccionario = {
    'nombre' : 'Soy Dalto', # clave : valor
    'canal' : 'Lucas Dalto',
    'esta_emocionado' : True,
    'altura' : 1.84,
    'dato_duplicado' : 'Soy Dalto',
}

print(diccionario['nombre']) # Se le da la clave (key)
