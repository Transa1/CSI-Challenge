# Diferentes tipos de variables
entero = 42
decimal = 3.1416
cadena = "Hola, Python"
booleano = True
lista = [1, 2, 3]
tupla = (10, 20)
diccionario = {"nombre": "Kevin", "edad": 22}
nulo = None

print(type(entero), type(decimal), type(cadena), type(diccionario))

print(f'Antes de cambio = {type(entero)}')
entero = 1.4142
print(f'Despues de cambio = {type(entero)}')
