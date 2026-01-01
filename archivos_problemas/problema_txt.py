#2 listas, una con nombres otra con apellidos. Se tienen que escribir los datos en un archivo de texto de forma óptima con un for

nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos =  ["Dalto","Zing","Dalto","Robetix","tarado"]

# Registrar este información en un archivo txt de forma óptima
with open("archivos_problemas/nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------------\n") for n, a in zip (nombres, apellidos)]