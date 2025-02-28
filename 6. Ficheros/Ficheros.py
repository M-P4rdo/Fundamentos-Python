#---------- Ficheros ----------
from io import open
import pathlib, shutil, os

#(Abrir):
var1 = str(pathlib.Path().absolute()) + "/6. Ficheros/ejemplo.txt"

if not os.path.exists(var1):
    datos = []
    for i in range(0, 50):
        datos.append(f"Linea {i+1}\n")
    archivo = open(var1, "w")
    archivo.writelines(datos)
    archivo.close()

#(Leer):
with open(var1, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()  #Todo el archivo
    contenido2 = archivo.readline() #Una Linea
    print(contenido)
    archivo.close()

with open(var1, "r", encoding="utf-8") as archivo:
    contenido3 = archivo.readlines() #Lista con todas las lineas
    #print(contenido)
    for i in range(0, 10): #Mostrar Lista
        print(f"{i+1}. {contenido3[i]}")
        archivo.close()

#(Escribir):
var2 = open(var1, "a+", encoding="utf-8") #Sin borrar
var2.write("Linea Extra\n")
var2.close()

with open("6. Ficheros/archivo.txt", "w", encoding="utf-8") as archivo: #Borrando
    archivo.write("Hola, mundo\n")
    archivo.close()

#(Manipular Archivos):
Archivo = str(pathlib.Path().absolute()) + "/6. Ficheros/ejemplo.txt"

lugarCopiar = "6. Ficheros/ejemplo2.txt"
shutil.copyfile(Archivo, lugarCopiar) #Copiar

#shutil.move("6. Ficheros/archivo.txt", "./archivo.txt") #Mover

if os.path.exists("6. Ficheros/ejemplo2.txt"): #Eliminar
    os.remove("6. Ficheros/ejemplo2.txt")

#(Json):
import json

var3 = str(pathlib.Path().absolute()) + "/6. Ficheros/datos.json"
data = {"nombre": "Alice", "edad": 25} #Guardar
with open(var3, "w") as file:
    json.dump(data, file, indent=4)
    file.close()

with open(var3, "r") as file: #Leer
    data = json.load(file)
    print(data)
    file.close()