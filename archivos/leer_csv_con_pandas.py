import pandas as pd

# Usando la función read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv") # df es de dataframe, que son estructuras de datos bidemnsionales (como hojas de cálculo) de filas y columnas
df2 = pd.read_csv("archivos/datos.csv") # También se puede usar la barra normal /

# Obteniendo los datos de la columna nombre
nombres = df["nombre"]

# Ordenadndolo de forma ascendente
df_ordenado = df.sort_values("edad") # Se crea un valor anonimo, por lo que se debe asignar a una variable

# Ordenandolo de forma descendente
df_ordenado = df.sort_values("edad", ascending=False) # El segundo argumento (ascending) es opcional, por defecto es True, que es ascendente, pero si se pone False, es descendente



# Concatenando los 2 dataframes
# El método concat une dataframes, ya sea por filas o por columnas, que pide como parámetro una lista de dataframes
df_concatenado = pd.concat([df, df2]) # Se pueden concatenar varios dataframes a la vez, pero en este caso se concatenan 2



# Accediendo a las primeras 3 filas con head()
# Si se pone 0, devuelve solo la estructura de columnas sin datos:
'''
Empty DataFrame
Columns: [nombre, apellido, edad]
Index: []
'''
primera_fila = df.head(3) # Devuelve las primeras n filas, por defecto n=5, pero si se pone 1, devuelve solo la primer fila, si se pone 3, devuelve las primeras 3 filas, y así sucesivamente


# Accediendo a las últimas 3 filas con tail()
ultima_fila = df.tail(3) # Devuelve las últimas n filas, es parecido a head(), pero devuelve las últimas filas en lugar de las primeras



# Accediendo a la cantidad de filas y columnas con shape
# Shape es un atributo (como una variable del objeto) que devuelve una tupla con la cantidad de filas y columnas del dataframe
filas_y_columnas_totales = df.shape # Devuelve una tupla (filas, columnas)
filas_totales, columnas_tales = filas_y_columnas_totales # Se desempaqueta la tupla en 2 variables: filas_totales y columnas_totales



# Obteniendo data estadística del dataframe con describe()
df_info = df.describe() # Devuelve un nuevo dataframe con estadísticas descriptivas del dataframe original, como la media, desviación estándar, valores mínimos y máximos, y los percentiles 25, 50 y 75 para cada columna numérica del dataframe


# loc es un método que permite acceder a un grupo de filas y columnas por etiquetas o una matriz booleana
# iloc es un método que permite acceder a un grupo de filas y columnas por posiciones enteras (índices)

# Accediendo a un elemento específico del df con loc
elemento_especifico_loc = df.loc[2, "edad"] # Accede al elemento en la fila con índice 2 (contando desde 0) y la columna "edad"

# Accediendo a un elemento específico del df con iloc
elemento_especifico_iloc = df.iloc[2, 2] # Accede al elemento en la fila con índice 2 y la columna con índice 2 (contando desde 0)


# Accediendo a todas las filas de una columna con iloc
apellidos = df.iloc[:, 1] # Se accede a todas las filas (:) de la columna con índice 1 (segunda columna, apellido)

# Accediendo a la fila 3 con loc
fila_3 = df.loc[2, :] # Se accede a la fila con índice 2 y todas las columnas (:)

fila_3 = df.iloc[2] # También se puede usar iloc para acceder a la fila 3


# Accediendo a filas con la edad mayor a 30
mayor_que_30 = df.loc[df["edad"]>30,:] # Se usa una condición booleana para filtrar las filas donde la edad es mayor a 30

print(fila_3)
