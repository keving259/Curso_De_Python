# Para usar append (agregar) se usa "a"
with open("archivos\\texto_de_dalto.txt", 'a', encoding='utf-8') as archivo:
    # Usando un bucle para agregar varias líneas
    [archivo.write(f"\nLínea {i+1} agregada") for i in range(5)]
