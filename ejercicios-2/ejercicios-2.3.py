#creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0] # El primer valor de la serie de fibonacci es 0, así que simplemente se pone en la lista al definirla
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(20)
print(resultado)
