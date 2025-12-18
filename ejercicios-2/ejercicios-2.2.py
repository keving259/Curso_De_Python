#creando una funciòn que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    # Verificamos que el número pasado no pueda dividirse por ningún número entre 2 y ese mismo número -1
    for i in range(2, num-1): # Un bucle que se ejecuta el número de veces que se pase menos 1 (para que no se divida entre sí mismo) desde 2, para que no divida entre 1, ya que todos los números son divisibles entre 1
        # Si es divisible por alguno retornamos False y termina el bucle
        if num%i == 0: return False # Si el resto es 0 significa que sí se pudo dividir por un número, por lo que no es primo, y se devuelve False
    # Si termina el bucle, significa que no fue divisible entonces es primo
    return True

# Creando función que retorne una lista con todos los primos
def primos_hasta(num):
    primos = []
    for i in range(1, num+1):
        # Verificamos si el valor es primo
        resultado = es_primo(i)
        # En caso de que sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        
    # Devolvemos la lista
    return primos

# Creamos el resultado llamando a la función y lo mostramos
resultado = primos_hasta(13)
print(resultado)
