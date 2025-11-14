# En lugar de usar bucles largos o temporales
palabras = ["Python", "es", "genial"]
longitudes = [len(p) for p in palabras]
print(longitudes)

# Enfoque pythonic: usar built-ins y expresividad
frase = " ".join(palabras)
print(frase)
