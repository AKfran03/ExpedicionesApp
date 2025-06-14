import csv

# Conjunto para guardar descripciones únicas
motivos_unicos = set()

# Leer expediciones.csv
with open("expediciones.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        descripcion = fila["motivo_terminacion"].strip()
        if descripcion:
            motivos_unicos.add(descripcion)

# Ordenar los motivos para tener un orden estable
motivos_ordenados = sorted(motivos_unicos)

# Escribir Motivo.csv
with open("Motivo.csv", "w", newline='', encoding="utf-8") as salida:
    campos = ["id_motivo", "descripcion"]
    escritor = csv.DictWriter(salida, fieldnames=campos)
    escritor.writeheader()

    for i, desc in enumerate(motivos_ordenados, start=1):
        escritor.writerow({"id_motivo": i, "descripcion": desc})

print("✅ Archivo 'Motivo.csv' generado correctamente.")
