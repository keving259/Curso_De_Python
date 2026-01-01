# El segundo parámetro "w" es para sobreescribir el contenido del archivo
with open("archivos\\texto_de_dalto.txt", 'w', encoding='utf-8') as archivo:
    # Sobreescribiendo el archivo
    #archivo.write("Jajaja te la recontra teclee")

    # Agregando 2 líneas con writelines
    archivo.writelines([" - Hola maestro como andas\n"," - misericordia\n"]) # A writelines se le pasa un iterable que escribe en la misma línea, pero se puede usar \n
    
    # Agregando otras 2 líneas
    archivo.writelines([" - no se porque dijiste eso\n"," - yo tampoco"])
