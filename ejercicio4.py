"""
EJERCICIO 4: Procesador de calificaciones

Crea una función llamada 'procesar_calificaciones' que reciba un diccionario
donde las claves son nombres de estudiantes y los valores son listas de calificaciones.

La función debe retornar un NUEVO diccionario donde cada clave sea el nombre
del estudiante y el valor sea su promedio de calificaciones (redondeado a 2 decimales).

Además, debe incluir una clave especial "mejor_estudiante" con el nombre del
estudiante con el promedio más alto.

Ejemplo:
procesar_calificaciones({
    "Ana": [85, 90, 88],
    "Luis": [70, 75, 72],
    "Maria": [95, 92, 98]
})
Debe retornar: {
    "Ana": 87.67,
    "Luis": 72.33,
    "Maria": 95.0,
    "mejor_estudiante": "Maria"
}
"""

def procesar_calificaciones(estudiantes):
    # Tu código aquí
    pass

# No modifiques el código de abajo - es para pruebas locales
if __name__ == "__main__":
    resultado = procesar_calificaciones({
        "Ana": [85, 90, 88],
        "Luis": [70, 75, 72],
        "Maria": [95, 92, 98]
    })
    print(resultado)