'''

'''

#creando un conjunto con set()
conjunto = set(["Dato 1"]) # Se converte la lista a conjunto
# No se pueden dar listas dentro de la lista, ya que son tipos de datos que se pueden modificar, los cual no permiten los sets. Sin embargo, se le pueden dar tuplas, ya que no cambian

#metiendo un conjunto dentro de otro conjunto
'''
Para hacer esto se usa la función frozenset(lista), con la que se crea un conjunto inmutable que está congelado para ser hasheable (modificable)
'''
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"} # Si no fuera frozenset daría error
print(conjunto2)



### Teoria de conjuntos
'''
Los subconjuntos tienen datos de un conjunto por separado. 
Si tiene los mismos dato más otros datos es un superconjunto.
Ej. A {2,4,6} es subconjunto del conjunto B {2,4,6,8,10} desde la persepectiva de A; y B es un superconjunto del conjunto A desde la persoectiva de B
'''

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,7,8}

#verificando si conjunto2 es un subconjunto de conjunto1
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1 # Es exactamente igual que .issubset()

#verificando si conjunto2 es un superconjunto de conjunto1 (lo contrario)
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1 # Es exactamente igual que .issuper()

#verificar si hay algùn nùmero en comun (isdisjoint)
resultado = conjunto2.isdisjoint(conjunto1)


print(resultado)
