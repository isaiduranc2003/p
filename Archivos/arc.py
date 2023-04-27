#./nombre de carpeta/ crear archivo dentro de la carpeta 
file = open("./Archivos/EjemploArchivo.txt", "w")
file.write("Esto es el contenido del archivo")
file.close()

lista = ["Fresa", "Kiwi", "Papaya"]
#with permite crear un contexto(crea una parte de ejecucion donde se va a utilizar el recurso utilizado)
with open("EjemploArchivo.txt", "a") as file:
    for e in lista:
        file.write(e + "\n")
#libera el recurso
#contexto conjunto de circunstancias
print("Archivo escrito")


lista2 = ["Honda", "Suzuki", "BMW"]
with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("lista escrita con writelines")


print("Imprimir todo el contenido del archivo.")
with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

#otros metodos

print("Leer archivo linea por linea") 
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline(2))#solo muestra las primeras 2 caracteres

#guardar contenido en forma de lista
print("Guardar contenido del archivo en una lista")
with open("EjemploArchivo.txt") as file:
    contenido = file.readlines()
    print(contenido)

#tarea hacer que la informacion (de las interfaces) se guarde en archivo de texto en un csv
#agregar un visor del archivo de la interfaz

#crear archivo csv
file = open("./Archivos/Archivo.csv", "w")
file.write("Esto es el contenido del archivo")
file.close()
