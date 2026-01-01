#si el modulo estuviera dentro de una carpeta en la misma ruta 

#import funciones_buenas.saludar as m_saludar # Se importa el modulo saludar

# Si está en una ruta atrás
import sys # Modulo built-in (integrado en Python)

sys.path.append("C:\\Users\\kevin\\OneDrive\\Escritorio\\a\\python\\Curso_De_Python-main\\Curso_De_Python\\funciones_buenas")
print(sys.path)

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))
