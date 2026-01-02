import re # Importamos el modulo de expresiones regulares

texto = '''Hola maestro. esta es la cadena 1. Como estas mi capitan
Esta es la linea 2662598 de texto.
Esta es la linea 2 de texto.
Y Esta es la final (linea 3) definitiva mi capitan'''

# Haciendo una búsqueda simple sin importar mayúsculas o minúsculas
resultado = re.findall("esta", texto, flags=re.IGNORECASE)

#\d - Busca digitos numéricos del 0 al 9
resultado = re.findall(r"\d", texto) # Con la r se indica que es una raw string

#\D - Busca cualquier caracter que no sea un dígito numérico
resultado = re.findall(r"\D", texto)

#\w -> Busca caracteres alfanuméricos (a-z A-Z 0-9 _)
resultado = re.findall(r"\w", texto)

#\W -> Busca cualquier caracter que no sea alfanumérico
resultado = re.findall(r"\W", texto)

#\s -> Busca espacios en blanco (espacios, tabulaciones, saltos de línea)
resultado = re.findall(r"\s", texto)

#\S -> Busca cualquier caracter que no sea un espacio en blanco
resultado = re.findall(r"\S", texto)

#. -> Busca cualquier caracter excepto saltos de línea
resultado = re.findall(r".", texto)

#\n -> Busca saltos de línea
resultado = re.findall(r"\n", texto)

#\ -> Cancelar caracteres especiales (lo que no es alfanumérico)
resultado = re.findall(r"\.", texto) # Cancelando la función especial del punto y buscando puntos literales

# Armando una cadena que busque un número, seguido de un punto y un espacio
resultado = re.findall(r"\d\.\s", texto)

# ^ -> Busca el inicio de una línea
# flags=re.M activa el modo multilínea
resultado = re.findall("Esta", texto, flags=re.M) # Indicando que busque al inicio de cada línea

# $ -> Busca el final de una línea
# flags=re.M activa el modo multilínea
resultado = re.findall("capitan$", texto, flags=re.M) # Indicando que busque al final de cada línea

# {n} -> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}\s', texto) # Busca 3 dígitos seguidos de un espacio

# {n, m} -> Busca entre n y m veces el valor de la izquierda
resultado = re.findall(r'\d{2,4}', texto) # Busca entre 1 y 4 dígitos seguidos

# Los grupos permiten agrupar patrones dentro de una expresión regular usando paréntesis
# Aquí buscamos el grupo 'ab' repetido entre 2 y 4 veces. Si no usamos grupos, buscaría solo la repetición del caracter 'b'
resultado = re.findall(r'(ab){2,4}', texto)

# [abc] -> Busca cualquiera de los caracteres dentro de los corchetes
resultado = re.findall(r'[ab]{2}', texto) # Busca combinaciones de 'a' y 'b' de 2 en 2

# | -> Operador OR, busca el patrón de la izquierda o el de la derecha
resultado = re.findall(r'\d{2,4}|Hola', texto) # Lo devuelve en el orden en que los encuentra

# * -> Busca el valor de la izquierda 0 o más veces
resultado = re.findall(r'ab*', texto) # Busca la 'a' seguida de

resultado = re.findall(r'^Esta.*texto\.\n', texto, flags=re.M) # Busca desde 'Esta' hasta 'texto.' en cada línea

print(resultado)