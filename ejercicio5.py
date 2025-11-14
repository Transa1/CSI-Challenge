"""
EJERCICIO 5: Manipulador de listas

Crea una función llamada 'manipular_lista' que reciba una lista de números
y realice las siguientes operaciones EN ORDEN:

1. Eliminar todos los números menores a 10
2. Multiplicar cada número restante por 2
3. Ordenar la lista de mayor a menor
4. Retornar solo los primeros 5 elementos

Si hay menos de 5 elementos, retorna todos los que haya.

Ejemplo:
manipular_lista([5, 15, 8, 23, 12, 30, 7, 18, 25])
Paso 1: [15, 23, 12, 30, 18, 25]
Paso 2: [30, 46, 24, 60, 36, 50]
Paso 3: [60, 50, 46, 36, 30, 24]
Paso 4: [60, 50, 46, 36, 30]
"""

def manipular_lista(numeros):
    # Tu código aquí
    pass

# No modifiques el código de abajo - es para pruebas locales
if __name__ == "__main__":
    resultado = manipular_lista([5, 15, 8, 23, 12, 30, 7, 18, 25])
    print(resultado)