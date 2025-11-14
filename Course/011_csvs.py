import csv

# Escribir un archivo CSV
with open("datosCSV.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["nombre", "edad"])
    writer.writerow(["Kevin", 22])
    writer.writerow(["Ana", 25])

# Leer un archivo CSV
with open("datosCSV.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        print(fila["nombre"], "tiene", fila["edad"], "años")
