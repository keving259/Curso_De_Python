import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# NOTA: Para archivos csv muy grandes, es recomendable utilizar pd.read_csv en conjunto con parámetros como chunksize (read_csv_in_chunks) o nrows para manejar la memoria de manera eficiente.

df = pd.read_csv('archivos_problemas_graficos/bigotes.csv')

sns.boxplot(x='categoria', y='valor', data=df)

plt.show()
# El gráfico de bigotes (boxplot) muestra la distribución de los datos en diferentes categorías.