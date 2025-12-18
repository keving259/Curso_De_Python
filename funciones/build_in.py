# Las funciones que ya están integradas dentro de Python por defecto, se llaman build in

numeros = [4,7,1]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)

#encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)

#redoneando a 6 decimales
numero = round(12.345678,3) # (número, decimales)

# bool()
#retorna False -> 0, vacio, False, None \ True -> distinto a 0, True, cadena, datos no vacio
resultado_bool = bool("sdsadsa")

# all()
#retorna True, si todos los valores son verdaderos
resultado_all = all([0,"true",[344,23]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)
