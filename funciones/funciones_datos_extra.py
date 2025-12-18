#creando una funcion de 3 parametros

def frase1(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#utilizando keyword arguments. Se especifica a que parámetro pertenece cada elemento, pero se debe especificar en todos
frase_resultante = frase1(adjetivo = "capo",nombre = "Lucas",apellido ="Dalto")


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase2(nombre,apellido,adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase2("Lucas","Dalto","inteligente")
print(frase_resultante)

