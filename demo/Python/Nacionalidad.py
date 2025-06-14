import csv

# Leer las nacionalidades únicas
nacionalidades_unicas = set()

with open("miembros.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        nacionalidad = fila["nacionalidad"].strip()
        if nacionalidad:
            nacionalidades_unicas.add(nacionalidad)

# Ordenar y asignar ID autoincremental
nacionalidades_ordenadas = sorted(nacionalidades_unicas)
nacionalidad_id_map = {nac: idx + 1 for idx, nac in enumerate(nacionalidades_ordenadas)}

# Escribir archivo Nacionalidad.csv
with open("Nacionalidad.csv", "w", newline='', encoding="utf-8") as archivo_salida:
    campos = ["id_nacionalidad", "descripcion"]
    escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
    escritor.writeheader()

    for nac, idn in nacionalidad_id_map.items():
        escritor.writerow({"id_nacionalidad": idn, "descripcion": nac})

print("✅ Archivo 'Nacionalidad.csv' generado correctamente.")
