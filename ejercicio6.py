"""
EJERCICIO 6: Generador de reporte desde CSV

Crea una función llamada 'generar_reporte' que:
1. Lea el archivo "ventas.csv" (que contiene columnas: producto, cantidad, precio)
2. Calcule el total de ventas de cada producto (cantidad * precio)
3. Retorne un diccionario con:
   - Cada producto como clave y su total de ventas como valor
   - Una clave especial "total_general" con la suma de todas las ventas

El archivo ventas.csv se verá así:
producto,cantidad,precio
Laptop,5,15000
Mouse,20,250
Teclado,15,800

Debe retornar:
{
    "Laptop": 75000,
    "Mouse": 5000,
    "Teclado": 12000,
    "total_general": 92000
}

IMPORTANTE: Primero debes crear el archivo ventas.csv con los datos del ejemplo
para que tu función pueda leerlo.
"""

import csv

def generar_reporte():
    # Tu código aquí
    pass

# No modifiques el código de abajo - es para pruebas locales
if __name__ == "__main__":
    # Primero crea el archivo ventas.csv manualmente o con este código:
    with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["producto", "cantidad", "precio"])
        writer.writerow(["Laptop", 5, 15000])
        writer.writerow(["Mouse", 20, 250])
        writer.writerow(["Teclado", 15, 800])
    
    resultado = generar_reporte()
    print(resultado)