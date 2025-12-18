'''
Lambda es como las funciones flecha de JS.
Con lambda se crean funciones "anónimas", porque no se les define un nombre
No es apta para varios 
'''

numeros = [1,2,3,4,5,6,7,8,9,11,13,14,15,20]

#creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

# Es lo mismo que hacer lo siguiente:
# def multiplicar_por_dos(x):
#     return x*2

# PERO lambda no devuelve el resultado, sino que devuelve un dato de tipo bool


#creando funcion comun que diga si es par o no
#def es_par(num):
#    if (num%2==0):
#        return True
    
#usando filter con una funcion comun
# filter es una función que permite filtrar elementos de un iterable basándose en una función de prueba que devuelve True o False, creando un nuevo iterador con solo los elementos que cumplen la función

# filter(funcion, iterable) <- La función debe devolver True o False
#numeros_pares = filter(es_par,numeros)



#creando lo mismo que antes pero con lambda
# Se crea una función anónima con un parámetro numero, se realiza la operación y se pregunta si es igual a 0 (True o False), y se pasa el iterable
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))
