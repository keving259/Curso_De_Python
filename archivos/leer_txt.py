# Se usa la función open para abirir el archivo. Sus parámetros son la ruta del archivo y la codificación
archivo = open("archivos\\texto_de_dalto.txt", encoding='utf-8') # Aquí Python crea un objeto archivo con un puntero de lectura, que empieza desde el inicio del archivo

# Leer archivo completo
#archivo = archivo.read() # El puntero está al final del archivo, porque ya fue leido

# Leer línea por línea
#lineas = archivo.readlines() # Igualmente, el puntero estaría al final

# Leer una sola línea
linea_1 = archivo.readline() # Solo lee la primer línea. Se le puede pasar un número, pero es para especificar los caracteres que se van a mostrar. Puede consumir mucha RAM. Ahora el puntero está en la seguna línea

# Para poner el puntero al principio
archivo.seek(0)

# Cerrar el archivo. Ya no se puede leer, a menos que se vuelva a abrir
archivo.close()
# Es importante cerrar el archivo porque el programa puede llegar a detenerse de forma inesperada y se pueden perder datos, o tampoco se podra abrir el archivo desde otro programa, ya que está en uso. También se liberan recursos

print(linea_1)
