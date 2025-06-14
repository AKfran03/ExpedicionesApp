import csv

accidentes_unicos = {}

# Leer expediciones.csv y recolectar accidentes únicos
with open("expediciones.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        accidente = fila["Accidente"].strip()
        if accidente and accidente not in accidentes_unicos:
            accidentes_unicos[accidente] = None  # Se asigna ID luego

# Asignar ID autoincremental
for idx, accidente in enumerate(accidentes_unicos.keys(), start=1):
    accidentes_unicos[accidente] = idx

# Escribir Accidente.csv
with open("Accidente.csv", "w", newline='', encoding="utf-8") as archivo_salida:
    campos = ["id_accidente", "descripcion"]
    escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
    escritor.writeheader()

    for descripcion, id_accidente in accidentes_unicos.items():
        escritor.writerow({
            "id_accidente": id_accidente,
            "descripcion": descripcion
        })

print("✅ Archivo 'Accidente.csv' generado correctamente.")
