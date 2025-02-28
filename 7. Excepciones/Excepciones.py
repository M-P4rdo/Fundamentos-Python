#---------- Manejo de Errores ----------
#(Específica):
try:
    lista = [1, 2, 3]
    print(lista[5]) #Error
except IndexError:
    print("Índice fuera de rango")

#(Multiple):
try:
    valor = int("Hola") #Error
except (ValueError, TypeError):
    print("Error de conversión de tipo")

#(Con Informacion):
try:
    resultado = 10 / 0 #Error
except ZeroDivisionError as e:
    print(f"Error: {e}")

#(Con Else):
try:
    num = int("5")
except ValueError:
    print("Error al convertir.")
else: #Si no hay excepcion
    print("Conversión exitosa:", num)
    
#(Con Finally):
try:
    f = open("archivo.txt", "r")
except FileNotFoundError:
    print("Archivo no encontrado.")
finally: #Se ejecuta Siempre
    print("Este bloque se ejecuta siempre.")

#(Personalizadas):
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Edad no permitida para el registro.")
    return "Acceso concedido."

try:
    print(verificar_edad(15))
except ValueError as e:
    print(f"Error: {e}")