# Creación de diccionarios
persona = {"nombre": "Kevin", "edad": 20, "pais": "México"}

# Otra forma
persona2 = dict(nombre="Ana", edad=25, pais="Chile")

# Acceso
print(persona["nombre"])
print(persona.get("correo", "No tiene correo"))

# Recorrido
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Operaciones
persona["edad"] += 1
persona["ocupacion"] = "Estudiante"
print(persona)
