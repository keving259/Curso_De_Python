import pandas as pd
import matplotlib.pyplot as plt # Librería de visualización de gráficos
import seaborn as sns # Librería para mejorar la estética de los gráficos estadísticos

df = pd.read_csv('archivos_problemas_graficos/pedos.csv')

# Creando el gráfico
sns.lineplot(x='fecha', y='pedos', data=df)

plt.plot('01-09', 17, 'o', color='red') # Punto destacado

plt.show()
