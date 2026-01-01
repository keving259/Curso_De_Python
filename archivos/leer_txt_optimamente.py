# Abriendo el archivo con with open
with open("archivos\\texto_de_dalto.txt", encoding='utf-8') as archivo:
    # Leemos el archivo
    contenido = archivo.read()
    print(contenido)

# No es necesario cerrarlo al usar with open