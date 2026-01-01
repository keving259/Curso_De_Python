#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")

# Convertir a string los datos de una columna
df['edad'] = df['edad'].astype('str')

# Mostrar el tipo de dato del primer elemento de la columna 'edad'
#print(type(df['edad'][0]))

# Reemplazado los datos dalto por "maestro"
df['apellido'].replace('dalto', 'maestro', inplace=True)

# Eliminar filas con datos faltantes
df = df.dropna()  # Eliminar filas con datos faltantes
# Por defecto dropna elimina filas con el valor axis=0, si se quiere eliminar columnas se usa axis=1

# Eliminar filas duplicadas
df = df.drop_duplicates()

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")
