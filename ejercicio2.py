"""
EJERCICIO 2: Filtrar nombres por longitud

Crea una función llamada 'filtrar_nombres' que reciba:
- Una lista de nombres (strings)
- Un número entero 'minimo'

La función debe retornar una NUEVA lista con solo los nombres que tengan 
una longitud mayor o igual a 'minimo', y además deben estar en MAYÚSCULAS.

Usa list comprehension para resolver este ejercicio.

Ejemplo:
filtrar_nombres(["Ana", "Roberto", "Luis", "Maria"], 5)
Debe retornar: ["ROBERTO", "MARIA"]
"""

def filtrar_nombres(nombres, minimo):
    # Tu código aquí
    pass

# No modifiques el código de abajo - es para pruebas locales
if __name__ == "__main__":
    resultado = filtrar_nombres(["Ana", "Roberto", "Luis", "Maria"], 5)
    print(resultado)