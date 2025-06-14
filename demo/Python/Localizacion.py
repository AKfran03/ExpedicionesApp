import csv

# Mapeo del valor del campo Host → id_host
host_map = {
    "China only": 1,
    "India only": 2,
    "Nepal": 3,
    "Nepal & China": 4,
    "Nepal & India": 5,
    "Nepal, China & India": 6
}

localizaciones = {}

# Leer picos.csv
with open("picos.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        descripcion = fila["Localizacion"].strip()
        host_str = fila["Host"].strip()
        id_host = host_map.get(host_str, 0)  # 0 si no está definido

        # Guardar solo localizaciones únicas con su respectivo id_host
        if descripcion not in localizaciones:
            localizaciones[descripcion] = id_host

# Escribir Localizacion.csv
with open("Localizacion.csv", "w", newline='', encoding="utf-8") as salida:
    campos = ["id_localizacion", "descripcion", "id_host"]
    escritor = csv.DictWriter(salida, fieldnames=campos)
    escritor.writeheader()

    for i, (descripcion, id_host) in enumerate(localizaciones.items(), start=1):
        escritor.writerow({
            "id_localizacion": i,
            "descripcion": descripcion,
            "id_host": id_host
        })

print("✅ Archivo 'Localizacion.csv' generado correctamente con id_host según el campo 'Host'.")
