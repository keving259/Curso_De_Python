import re

text = "remplazando todas las vocales por asteriscos"

new_text = re.sub("[aeiou]", "*", text) # Reemplaza todas las vocales por asteriscos

print(new_text)