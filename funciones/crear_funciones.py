
#creando una funciòn simple
def saludar():
    print("Hola lucas, mi maestro ¿Como andas?")

#ejecutando la funcion simple
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    
    
saludar("Camila","MuJER")
saludar("Dalto","hombre")
saludar("Fran","no binario")



#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0]) #  Del número que se ingrese solo se queda con el primer dígito
    c1 = num - 2 # En base al número se crean 3 caracteres
    c2 = num
    c3 = num - 5
    # Del string, se seleccionan caracteres según los números calculados en las c
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # Se retorna la contraseña y el número dado a la función para guardarlos
    return contraseña,num
    
#desempaquetando la funciòn
# Lo retornado de la función se guarda en las dos siguientes variables
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")
