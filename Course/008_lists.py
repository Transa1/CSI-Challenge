# ===== CREAR LISTAS =====
numeros = [1, 2, 3, 4, 5]
mixta = [1, "dos", 3.0, True]
vacia = []

# ===== ACCESO Y SLICING =====
print(numeros[0])      # primer elemento
print(numeros[-1])     # último elemento
print(numeros[1:4])    # sublista del índice 1 al 3
print(numeros[::2])    # cada 2 elementos
print(numeros[::-1])   # lista invertida

# ===== OPERACIONES DE ADICIÓN =====
numeros.append(6)           # agregar al final
numeros.insert(0, 0)        # insertar en posición
numeros.extend([7, 8])      # agregar múltiples elementos
nueva = numeros + [9, 10]   # concatenar listas

# ===== OPERACIONES DE ELIMINACIÓN =====
numeros.remove(3)      # eliminar primera ocurrencia del valor
ultimo = numeros.pop() # eliminar y retornar último elemento
del numeros[0]         # eliminar por índice

print("Lista final:", numeros)

# ===== MÉTODOS ÚTILES =====
frutas = ["manzana", "cereza", "banana", "cereza"]
print(frutas.count("cereza"))    # contar ocurrencias
print(frutas.index("banana"))    # encontrar índice
frutas.sort()                     # ordenar in-place
print(frutas)

# ===== FUNCIONES COMUNES =====
nums = [10, 20, 30, 40]
print(len(nums))      # longitud
print(sum(nums))      # suma
print(min(nums))      # mínimo
print(max(nums))      # máximo

# ===== RECORRER LISTAS =====
colores = ["rojo", "verde", "azul"]
for color in colores:
    print(color)

for i, color in enumerate(colores):
    print(f"Índice {i}: {color}")

# ===== LIST COMPREHENSION =====
cuadrados = [n**2 for n in range(1, 6)]
pares = [n for n in range(10) if n % 2 == 0]
print("Cuadrados:", cuadrados)
print("Pares:", pares)

# ===== OPERADORES =====
print("banana" in frutas)       # verificar si existe
print("kiwi" not in frutas)     # verificar si no existe

# ===== COPIAR LISTAS =====
original = [1, 2, 3]
copia = original.copy()         # crear copia
otra_copia = original[:]        # copiar con slicing

# ===== DESEMPAQUETADO =====
a, b, c = [1, 2, 3]
primero, *resto = [1, 2, 3, 4, 5]
print(f"Primero: {primero}, Resto: {resto}")