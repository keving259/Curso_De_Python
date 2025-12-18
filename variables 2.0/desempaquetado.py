'''
El desempaquetado de variabes es una técnica para asignar valores a variables. Crear variables nuevas a partir de arreglos, como listas, tuplas y conjuntos
'''
#creando los datos
datos_en_tupla = ("Lucas","Dalto",1000000)
datos_en_lista = ["Lucas","Dalto",1000000]

#desempaquetado
nombre,apellido,suscriptores = datos_en_lista # Se desempaquetan los datos y se asignan a las variables

#mostrando resultado
print(suscriptores)
