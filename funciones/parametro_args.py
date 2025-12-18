#forma no optima de sumar valores
# NO es óptimo porque se deberían poder pasar los argumentos que se deseen, y aquí se limita a pasar una lista
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

#resultado = suma([5,3,9,10,20,3])

# Utilizando parámetro args
# Toma todos los parámetros como si fueran uno solo. Se pone un * al inicio
def suma2(*numeros):
    return sum(numeros)

#resultado = suma(4,5,6,7,8,9) # Se puden dar varios parámetros

# ARGS SIEMPRE DEBE DE IR AL FINAL, no se pueden poner más parámetros segudos de args
def suma3(nombre, *numeros):
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"



#forma optima de sumar valores
# * se puede usar para expandir una estructura
def suma_total(numeros):
    print(*numeros) # Aquí * desempaqueta la lista de números, es lo mismo que hacer print(1, 2, 3). No imprime la lista, imprime los valores desempaquetados
    
    return sum([*numeros]) # Se le puede dar una lista con cualquier cantidad de valores, pero es lo mismo que usar simplemente sum(numeros)

resultado2 = suma_total([5,3,9,10,20,3])


#lo mismo que arriba pero utilizando el operador * como parametro (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Lucas",5,3,9,10,20,3)
