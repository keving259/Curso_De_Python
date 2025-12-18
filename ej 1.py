lista = list()

def mult(lista):
    result = 1
    lista_final = list()
    for i in lista:
        result *= result * i
        lista_final.append(result)
    print(lista_final)

prueba = mult([1,2,3,4])