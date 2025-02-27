#---------- Estructuras de Datos ----------
#(Lista):
lista = [1, 2, 3, "Python", True]
listaNumerica = list(range(0, 5))

lista.append(6) #Agregar
lista.insert(2, "Si")
lista[3] = "x2" 

print(lista[0:6])
print(lista)
for item in lista: #Recorrer
    print(item)

lista.remove("Si") #Eliminar
lista.pop(0) #Eliminar por Posicion

listaNumerica.extend(lista) #Unir Listas
print(listaNumerica)

#(Diccionario):
diccionario = { "Nombre": "Miguel", "Apellido": "Pardo", "Edad": 20}

diccionario["Cumpleaños"] = "15 Mayo" #Agregar
diccionario["Nombre"] = "Angel"

print(diccionario["Edad"])
print(diccionario)
for clave, valor in diccionario.items(): #Recorrer
    print(f"{clave} : {valor}")

del diccionario["Cumpleaños"] #Eliminar

#(Tupla):
tupla = ("Miguel", "Pardo", 20)

print(tupla[2])
for i, valor in enumerate(tupla): #Recorrer
    print(f"Índice {i}: {valor}")

#(Conjunto):
set = {"Miguel", "Pardo", 20}

set.add("15 Mayo") #Agregar

print(set)
for valor in set: #Recorrer
    print(valor)

set.discard("15 Mayo") #Eliminar

#(Lista Con Diccionarios):
x1 = [{"Dia": "Lunes", "Mes" : "Abril"},{"Dia": "Jueves", "Mes" : "Junio"}]
print(x1[0]["Dia"])

#(Diccionario Con Listas):
x2 ={"Dia":["Lunes", "Martes", "Miercoles"], "Año" : ["2021", "2022", "2023"]}
print(x2["Año"][1])

#---------- Estructuras Avanzadas ----------
#(Doble Cola):
from collections import deque

mi_deque = deque([1, 2, 3])
mi_deque.appendleft(0)  # Inserta al inicio
mi_deque.append(4)  # Inserta al final
print(mi_deque)

mi_deque.pop()  # Elimina del final

#(Diccionario Predeterminado):
from collections import defaultdict

mi_defaultdict = defaultdict(int)  # Valores por defecto
mi_defaultdict["a"] += 1  # No da error si "a" no existía
print(mi_defaultdict["a"])  # Imprime 1

#(Contador):
from collections import Counter

contador = Counter("banana")
print(contador)  # {'b': 1, 'a': 3, 'n': 2}

#---------- Estructuras Multidimecionales ----------
#(Lista):
contactos = [['Luis', 'luis@mail.com'], ['Thomas', 'thomas@mail.com'],
              ['Miguel', 'miguel@mail.com']]

contactos.append(['Heider', 'heider@mail.com']) #Añadir
contactos[2][0] = 'Angel'
print(f"Nombre: {contactos[1][0]}")
print(f"Correo: {contactos[1][1]}")
print(contactos)

for contacto in contactos: #Recorrer
    for elemento in contacto:
        print(elemento, end=" ")

del contactos[0] #Eliminar

#(Diccionario):
informacion = {
    "Clave1" : {"Nombre": "Thomas", "Apellido": "Gil", "Edad": 22},
    "Clave2" : {"Nombre": "Daniel", "Apellido": "Pardo", "Edad": 20},
    "Clave3" : {"Nombre": "Maicol", "Apellido": "Torres", "Edad": 21}
}

informacion["Clave4"] = {"Nombre": "Isabella", "Apellido": "Gallego", "Edad": 19} #Añadir
informacion["Clave3"]["Apellido"] = "Macondo"
print(informacion["Clave2"]["Apellido"])
print(informacion)

for clave, valor in informacion.items(): #Recorrer
    print(clave, end=" ")
    for info in valor.items():
        print(f"{info}", end=" ")
    print()

del informacion["Clave3"] #Eliminar
del informacion["Clave4"]["Nombre"]

