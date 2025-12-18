
#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]


#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue    # Si fruta es manzana ejecuta continue. Con continue se salta manzana y continua con la ejecución del bucle 
    print(f'Me voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break   # Si furta es pera se rompe el bucle
else: 
    print("terminado") # Cuando se rompe el bucle tampoco llega al else



#recorer una cadena de texto
cadena = "Hola Dalto"

for letra in cadena:
    print(letra)



# LIST COMPREHENSION
#for en una sola linea de còdigo (duplicamos los numeros)
numeros = [2,5,8,10]

# Crea una nueva lista tomando cada x de numeros y guardando x * 2
numeros_duplicados = [x*2 for x in numeros] # [expresión (x*2) for i (x) in variable (numeros)]
# x*2 <- es la expresión que se guarda en la nueva lista
# for x in numeros <- el bucle recorre la lista orginal
# lo que se quiere guardar - para cada elemento - en esta lista
print(numeros_duplicados)


nums = [1,2,3]

nums_al_cuadrado = [n**2 for n in nums]
print(nums)
