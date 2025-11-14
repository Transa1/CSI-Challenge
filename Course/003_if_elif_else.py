# Ejemplo simple de condiciones

edad = input("Cual es tu edad ")

edad = int(edad)

if edad < 18:
    print("Eres menor de edad")
elif edad < 30:
    print("Eres joven adulto")
else:
    print("Eres adulto")
