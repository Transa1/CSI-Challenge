"""
EJERCICIO 3: Contador de palabras en una frase

Crea una función llamada 'contar_palabras' que reciba un string (frase)
y retorne un diccionario donde las claves sean las palabras (en minúsculas)
y los valores sean el número de veces que aparece cada palabra.

Pistas:
- Usa .lower() para convertir a minúsculas
- Usa .split() para separar las palabras
- Los diccionarios pueden usar .get() para contar

Ejemplo:
contar_palabras("Hola mundo hola Python")
Debe retornar: {"hola": 2, "mundo": 1, "python": 1}
"""

def contar_palabras(frase):
    # Tu código aquí
    pass

# No modifiques el código de abajo - es para pruebas locales
if __name__ == "__main__":
    resultado = contar_palabras("Hola mundo hola Python")
    print(resultado)