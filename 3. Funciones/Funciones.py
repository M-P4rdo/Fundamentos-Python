#---------- Funciónes ----------
#(Simples):
def saludar_s():
    print("¡Hola, bienvenido!")

#(Con Parámetros):
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

#(Con Retorno):
def suma(a, b):
    return a + b

#(Valores Predeterminados):
def presentar(nombre="Desconocido"):
    print(f"Hola, soy {nombre}.")

#(Con *Args (Argumentos Variables Posicionales)):
def sumar_todo(*numeros):
    return sum(numeros)

#(Con **Kwargs (Argumentos Variables con Nombre)):
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

#(Lambda):
doble = lambda x: x * 2

numeros = [1, 2, 3, 4, 5]
numeros_mas_10 = list(map(lambda x: x + 10, numeros)) #(Lambda con map)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) #(Lambda con filter)

#(Anidados):
def exterior():
    def interior():
        print("Soy la función interior")
    interior()

#(Retorna Multiples Valores):
def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

#(Devuelve Otras Funciones):
def operacion(tipo):
    if tipo == "suma":
        return lambda a, b: a + b
    elif tipo == "multiplicacion":
        return lambda a, b: a * b

#(Generadoras):
def contador():
    for i in range(3):
        yield i

#(Decoradores):
def decorador(func):
    def envoltura():
        print("Antes de la función")
        func()
        print("Después de la función")
    return envoltura

@decorador
def saludo():
    print("¡Hola!")

#---------- Llamar las Funciónes ----------
saludar_s() #Simples
saludar("Carlos") #Parametro
print(suma(5, 3)) #Retorno
presentar() #Valor Predeterminado
presentar("Ana") #Valor Predeterminado
print(sumar_todo(1, 2, 3, 4, 5)) #*Args
mostrar_info(nombre="Luis", edad=30) #*Kwargs
print(numeros_mas_10) #Lambda con Map
print(numeros_pares) #Lambda con Filter
exterior() #Anidado
suma_1, resta_1 = calcular(5, 3) #Devuelve Multiples Valores
print(suma_1, resta_1)
sumar = operacion("suma") #Devuelve Otra Funcion 
print(sumar(5, 3))
for numero in contador(): #Generadora
    print(numero)
saludo() #Decorador