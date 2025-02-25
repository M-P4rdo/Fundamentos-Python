#---------- Modulos ----------
#(Argumentos de Línea de Comandos):
import sys

print("Nombre del script:", sys.argv[0])
if len(sys.argv) > 1:
    print("Argumentos:", sys.argv[1:])
else:
    print("No se pasaron argumentos.")

#(Manejo del Tiempo):
import time

print("Inicio...")
time.sleep(2)  #Pausa de 2 segundos
print("Pasaron 2 segundos")

#(Manejo de Fechas):
import datetime

print(datetime.date.today())
Var = datetime.datetime.now()
print(Var.year, 
      Var.month, 
      Var.day, 
      Var.hour, 
      Var.minute, 
      Var.second) #Valores de la Fecha (Var)
Var = Var.strftime("%d/%m/%Y") #Comandos de Fromateo

#(Operaciones Matemáticas):
import math

print("Raíz cuadrada de 25:", math.sqrt(25))
print("Valor de pi:", math.pi)
print("Factorial de 5:", math.factorial(5))

#(Generación Aleatoria):
import random

print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
print("Elemento aleatorio de una lista:", random.choice(["rojo", "verde", "azul"]))

#(Iteradores y Combinaciones):
import itertools

combinaciones = itertools.combinations("ABC", 2)
print("Combinaciones:", list(combinaciones))

permutaciones = itertools.permutations("ABC", 2)
print("Permutaciones:", list(permutaciones))

producto = itertools.product([1, 2], ["A", "B"])
print("Producto cartesiano:", list(producto))

#(Json):
import json

datos = {"nombre": "Juan", "edad": 30, "activo": True}
json_str = json.dumps(datos) #Serialización
print("JSON:", json_str)

datos_cargados = json.loads(json_str) #Deserialización
print("Diccionario:", datos_cargados)