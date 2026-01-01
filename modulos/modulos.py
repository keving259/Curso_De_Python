#importando un modulo y asignandole el nombre "m_saludar"

# Desde ese modulo se importan dos funciones y les cambiamos el nombre from
from modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_coscu
import modulos.modulo_saludar as m_saludar

# Creamos las variables con los saludos
saludo = saludar_normal("Lucas")
saludo_raro = saludar_como_coscu("Fran")

# Mostramos los resultados
print(saludo)
print(saludo_raro)

# Para vere las propiedades y métodos del namespace
#print(dir(m_saludar))

# Se accede al nombre del modulo que se importó
print(__name__)

# Se accede al nombre del modulo llamado
print(m_saludar.__name__)
