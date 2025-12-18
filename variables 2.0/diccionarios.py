#creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto") # clave=valor

# Las claves no deben de ser mutables (no deben modificarse)

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","rancio" ]):"jajas"}

# Se pueden usar tuplas porque no son mutables
diccionario = {("dalto","rancio" ):"jajas"}

#creando diccionarios con dict.fromkeys() valor por defecto: none
# Permite crear un diccionario con todos los valores none
# Se debe usar una lista. Si se usara un string, asignaría una clave por caracter. Ej. nombre, crea n=none, o=none, m=none...
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)
