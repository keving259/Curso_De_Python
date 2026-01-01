import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_graficos/cofla_ingresos.csv')

# Creando el gráfico de barras
sns.barplot(x='fuente', y='ingresos', data=df)

# Obteniendo el total de ingresos
total_ingresos = df['ingresos'].sum() # Suma todos los ingresos

# Mostrando el total de ingresos en la consola
print(f'El total de ingresos es de: ${total_ingresos} USD')

# Mostrando el gráfico
plt.show()
