import re

email = "lucasdaltonuevogmail@gmail.com"

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
# + significa que debe haber al menos una coincidencia
# [a-zA-Z0-9._%+-]+ indica que se debe cumplir [a-zA-Z0-9._%+-] al menos una vez
# 2, indica que debe haber al menos dos caracteres en la extensión del dominio, pero puede haber más


result = re.match(pattern, email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")