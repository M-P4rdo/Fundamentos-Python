#---------- Visualizar informacion ----------
#(Mostrar Texto):
print("Hola Mundo")
#(Obtener Datos):
db = input("Ingresa un texto: ")

#---------- Asignacion de Variables ----------
#(Basicos):
v1 = 8 
v2 = 6
v3 = 4
suma = 0; resta = 0; divi = 0; multi = 0; sobrante = 0
#(Multiple):
a, b, c = 1, 2, 3
nombre, edad = "Juan", 25
#(Mismo Valor):
x = y = z = 5

#---------- Tipos de Datos ----------
t0 = 'a'
t1 = "Texto" #Cadena de Texto (string)
t2 = 2 #Entero (int)
t3 = 10/4 #Flotante (float)
t4 = True #Booleano (bool)
t5 = None #Vacio
t6 = 3 +2j #Complejo (complex)
t7 = [1, 2, 3, 4, 5] #Lista (list)
t8 = (10.5, 20.3) #Tupla (tuple)
t9 = range(5) #Rango = (0, 1, 2, 3, 4)
t10 = {"manzana", "pera", "uva"} #Colección (set)
t11 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} #Diccionario (dict)
print(type(t6)) #Tipo de dato

#---------- Concatenacion ----------
#(Numeros):
print(t1 + " " + t0 + f" {t3} {t4} {t5}")
print(f"Los Numeros son {v1}, {v2}, {v3}")
print("Los Numeros son {}, {}, {}".format(v1, v2, v3))
#(Texto):
print(t1 + " de prueba")

#---------- Opreadores ----------
x = 5; y = 3
#(Aritmeticos):
suma = v1 + v2
resta = v2 - v3
multi = v1 * v2
divi = v3 / v1 #Devuelve Decimales
divi2 = v3 // t3 #Devuelve Enteros
sobrante = v2 % v3 #Muestra el residuo de la division
elevado = v2 ** v3 #Eleva el primer numero al segundo (6 a la 4)
#(Comparacion):
igualdad = (x == y)
diferente = (x != y)
mayor_que = (x > y)
menor_que = (x < y)
mayor_o_igual = (x >= y)
menor_o_igual = (x <= y)
#(Logicos):
Y = (x > 2) and (y < 5)
O = (x > 10) or (y < 5)
No = not (x > 2)
#(Asignacion):
x += 2 #Suma y asigna
x -= 2 #Resta y asigna	
x *= 2 #Multiplica y asigna
x /= 2 #Divide y asigna	
x //= 2	#División entera y asigna	
x %= 2 #Módulo y asigna	
x **= 2 #Potencia y asigna

#---------- Conversion de Datos ---------- 
d1 = int("2")
d2 = float("2")
d3 = str([1,2,3])
d4 = bool(0)
d5 = list("Texto")
d6 = tuple([1,2,3])
d7 = set([1,1,2,3,3])
d8 = dict([("nombre", "Juan"), ("edad", 25)])
print(f"{d1}\n{d2}\n{d3}\n{d4}\n{d5}\n{d6}\n{d7}\n{d8}\n")
