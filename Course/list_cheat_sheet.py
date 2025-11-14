# ============================================
# GUÍA COMPLETA DE LISTAS EN PYTHON
# ============================================

print("=" * 50)
print("1. CREAR LISTAS")
print("=" * 50)

# Listas vacías
vacia1 = []
vacia2 = list()

# Listas con elementos
numeros = [1, 2, 3, 4, 5]
mixta = [1, "dos", 3.0, True, None]
anidada = [[1, 2], [3, 4], [5, 6]]

# Crear lista desde otros iterables
desde_string = list("Python")
desde_range = list(range(5))
print("Desde string:", desde_string)
print("Desde range:", desde_range)

print("\n" + "=" * 50)
print("2. ACCESO A ELEMENTOS")
print("=" * 50)

frutas = ["manzana", "banana", "cereza", "durazno", "uva"]
print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])
print("Penúltima:", frutas[-2])

# Verificar existencia
print("'banana' está en la lista:", "banana" in frutas)
print("'kiwi' NO está en la lista:", "kiwi" not in frutas)

print("\n" + "=" * 50)
print("3. SLICING (REBANADO)")
print("=" * 50)

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista original:", nums)
print("Del índice 2 al 5:", nums[2:6])
print("Desde el inicio hasta 4:", nums[:5])
print("Desde 6 hasta el final:", nums[6:])
print("Todos los elementos:", nums[:])

# Slicing con step
print("\nCon step:")
print("Cada 2 elementos:", nums[::2])
print("Del 1 al 8 cada 2:", nums[1:9:2])
print("Lista invertida:", nums[::-1])
print("Del 7 al 2 invertido:", nums[7:1:-1])

# Slicing para copiar
copia = nums[:]
print("Copia de lista:", copia)

print("\n" + "=" * 50)
print("4. MODIFICAR LISTAS")
print("=" * 50)

colores = ["rojo", "verde", "azul"]
print("Original:", colores)

# Cambiar un elemento
colores[1] = "amarillo"
print("Después de cambiar índice 1:", colores)

# Cambiar varios elementos con slicing
colores[0:2] = ["naranja", "morado"]
print("Después de cambiar slice:", colores)

print("\n" + "=" * 50)
print("5. MÉTODOS DE ADICIÓN")
print("=" * 50)

lista = [1, 2, 3]
print("Inicial:", lista)

# append - agregar al final
lista.append(4)
print("Después de append(4):", lista)

# insert - insertar en posición específica
lista.insert(0, 0)
print("Después de insert(0, 0):", lista)

# extend - agregar múltiples elementos
lista.extend([5, 6, 7])
print("Después de extend([5,6,7]):", lista)

# Concatenación con +
nueva = lista + [8, 9]
print("Concatenación con +:", nueva)

# Repetición con *
repetida = [1, 2] * 3
print("Repetición [1,2]*3:", repetida)

print("\n" + "=" * 50)
print("6. MÉTODOS DE ELIMINACIÓN")
print("=" * 50)

letras = ['a', 'b', 'c', 'd', 'e', 'c']
print("Original:", letras)

# remove - elimina primera ocurrencia
letras.remove('c')
print("Después de remove('c'):", letras)

# pop - elimina y retorna elemento por índice
ultimo = letras.pop()
print(f"Pop sin índice (último): {ultimo}, lista:", letras)

segundo = letras.pop(1)
print(f"Pop(1): {segundo}, lista:", letras)

# del - elimina por índice o slice
del letras[0]
print("Después de del letras[0]:", letras)

# clear - vacía la lista
letras_temp = ['x', 'y', 'z']
letras_temp.clear()
print("Después de clear():", letras_temp)

print("\n" + "=" * 50)
print("7. MÉTODOS DE BÚSQUEDA Y CONTEO")
print("=" * 50)

numeros = [1, 3, 5, 3, 7, 3, 9]
print("Lista:", numeros)

# index - encuentra índice de primera ocurrencia
indice = numeros.index(3)
print("Índice de 3:", indice)

# index con inicio y fin
indice2 = numeros.index(3, 2, 6)  # buscar desde índice 2 hasta 6
print("Índice de 3 (desde pos 2):", indice2)

# count - cuenta ocurrencias
cantidad = numeros.count(3)
print("Cantidad de veces que aparece 3:", cantidad)

print("\n" + "=" * 50)
print("8. ORDENAMIENTO Y REVERSIÓN")
print("=" * 50)

desordenada = [3, 1, 4, 1, 5, 9, 2, 6]
print("Original:", desordenada)

# sort - ordena in-place (modifica la original)
desordenada.sort()
print("Después de sort():", desordenada)

desordenada.sort(reverse=True)
print("sort(reverse=True):", desordenada)

# sorted - retorna nueva lista ordenada
otra = [5, 2, 8, 1]
ordenada = sorted(otra)
print("sorted() - original:", otra, "nueva:", ordenada)

# reverse - invierte in-place
desordenada.reverse()
print("Después de reverse():", desordenada)

# Ordenar por criterio personalizado
palabras = ["python", "es", "un", "lenguaje"]
palabras.sort(key=len)
print("Ordenadas por longitud:", palabras)

print("\n" + "=" * 50)
print("9. FUNCIONES ÚTILES CON LISTAS")
print("=" * 50)

nums = [10, 20, 30, 40, 50]
print("Lista:", nums)
print("len() - longitud:", len(nums))
print("sum() - suma:", sum(nums))
print("min() - mínimo:", min(nums))
print("max() - máximo:", max(nums))

# any y all
booleanos = [True, False, True]
print("\nLista booleanos:", booleanos)
print("any() - alguno True:", any(booleanos))
print("all() - todos True:", all(booleanos))

print("\n" + "=" * 50)
print("10. ITERAR LISTAS")
print("=" * 50)

frutas = ["manzana", "banana", "cereza"]

# Forma básica
print("Iteración básica:")
for fruta in frutas:
    print(f"  - {fruta}")

# Con enumerate (índice y valor)
print("\nCon enumerate:")
for i, fruta in enumerate(frutas):
    print(f"  {i}: {fruta}")

# enumerate con inicio personalizado
print("\nCon enumerate(start=1):")
for i, fruta in enumerate(frutas, start=1):
    print(f"  {i}. {fruta}")

# Iterar múltiples listas con zip
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]
print("\nCon zip:")
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

print("\n" + "=" * 50)
print("11. LIST COMPREHENSION")
print("=" * 50)

# Básico
cuadrados = [x**2 for x in range(1, 6)]
print("Cuadrados:", cuadrados)

# Con condición
pares = [x for x in range(10) if x % 2 == 0]
print("Números pares:", pares)

# Con if-else
paridad = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print("Paridad:", paridad)

# Múltiples condiciones
nums_especiales = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print("Divisibles por 2 y 3:", nums_especiales)

# Transformación de strings
palabras = ["python", "java", "c++"]
mayusculas = [p.upper() for p in palabras]
print("Mayúsculas:", mayusculas)

# Comprensión anidada (matrices)
matriz = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matriz 3x3:")
for fila in matriz:
    print(" ", fila)

# Aplanar lista anidada
anidada = [[1, 2, 3], [4, 5], [6, 7, 8]]
aplanada = [num for sublista in anidada for num in sublista]
print("Lista aplanada:", aplanada)

print("\n" + "=" * 50)
print("12. DESEMPAQUETADO")
print("=" * 50)

# Desempaquetado básico
a, b, c = [1, 2, 3]
print(f"a={a}, b={b}, c={c}")

# Con * (resto)
primero, *resto = [1, 2, 3, 4, 5]
print(f"primero={primero}, resto={resto}")

primero, *medio, ultimo = [1, 2, 3, 4, 5]
print(f"primero={primero}, medio={medio}, ultimo={ultimo}")

# Intercambiar valores
x, y = 10, 20
x, y = y, x
print(f"Después de intercambiar: x={x}, y={y}")

print("\n" + "=" * 50)
print("13. LISTAS ANIDADAS")
print("=" * 50)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz completa:", matriz)
print("Fila 0:", matriz[0])
print("Elemento [1][2]:", matriz[1][2])

# Iterar matriz
print("Iterando matriz:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

print("\n" + "=" * 50)
print("14. COPIAS DE LISTAS")
print("=" * 50)

original = [1, 2, 3, [4, 5]]

# Copia superficial (shallow copy)
copia1 = original.copy()
copia2 = original[:]
copia3 = list(original)

# Modificar lista anidada afecta copias superficiales
original[3][0] = 99
print("Original:", original)
print("Copia1:", copia1)  # También cambió el [99, 5]

# Copia profunda (deep copy) para listas anidadas
import copy
original2 = [1, 2, [3, 4]]
copia_profunda = copy.deepcopy(original2)
original2[2][0] = 100
print("\nOriginal2:", original2)
print("Copia profunda:", copia_profunda)  # No se afecta

print("\n" + "=" * 50)
print("15. TIPS Y TRUCOS")
print("=" * 50)

# Eliminar duplicados manteniendo orden
con_duplicados = [1, 2, 2, 3, 1, 4, 3, 5]
sin_duplicados = list(dict.fromkeys(con_duplicados))
print("Sin duplicados:", sin_duplicados)

# Filtrar valores None o falsy
con_nones = [1, None, 2, "", 3, 0, False, 4]
sin_nones = [x for x in con_nones if x]
print("Sin valores falsy:", sin_nones)

# Unir lista de strings
palabras = ["Hola", "mundo", "Python"]
frase = " ".join(palabras)
print("Join:", frase)

# Dividir string en lista
texto = "uno,dos,tres"
lista_texto = texto.split(",")
print("Split:", lista_texto)

# Encontrar índices de todas las ocurrencias
lista = [1, 2, 3, 2, 4, 2, 5]
indices = [i for i, x in enumerate(lista) if x == 2]
print("Índices donde está 2:", indices)

print("\n" + "=" * 50)
print("FIN DE LA GUÍA")
print("=" * 50)