#---------- Condicionales ----------
a = int(input("Primer Numero: "))
b = int(input("Segundo Numero: "))

#(If - elif - else):
if b > 0:
    print(f"Su división es: {a / b}")
elif b < 0:
    print("No puedo dividir entre negativos")
else:
    print("No se puede dividir entre 0")

#(Multiples):
hora = 14; dia = "sábado"
if hora >= 9 and hora <= 17:
    print("Es horario laboral")

if dia.lower() in {"sábado", "domingo"}:
    print("Es fin de semana")

#(Anidados):
edad = 20; identificacion = True
if edad >= 18:
    if identificacion:
        print("Puedes ingresar")
    else:
        print("Necesitas identificación")
else:
    print("No puedes ingresar")

#(Operador Ternario):
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

#---------- Bucle For ----------
#(Rango):
for i in range(5):
    print(f"Iteración {i}") #(0 ~ 4)

#(Elemento Iterable):
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

#(Cadena de Texto):
for letra in "Texto":
    print(letra)

#---------- Bucle While ---------- 
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  #Incrementa el contador

#---------- Control de Bucles ---------- 
#(Break):
for i in range(10):
    if i == 5:
        print("Se detiene en 5")
        break  #Sale del bucle cuando i es 5
    print(i)

#(Continue):
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  #Salta la impresión de 3
    print(contador)

#(Pass):
for i in range(5):
    if i == 2:
        pass  #El pass no afecta la ejecución del código
    print(i)

