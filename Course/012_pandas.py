import pandas as pd

# Leer un CSV
df = pd.read_csv("datos.csv")
print(df)

# Modificar una columna
df["edad"] = df["edad"].astype(int) + 1

# Guardar en un nuevo archivo
df.to_csv("datos_modificados.csv", index=False)

print("Archivo modificado guardado exitosamente.")
