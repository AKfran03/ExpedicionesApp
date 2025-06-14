import csv

fechas_unicas = {}

with open("expediciones.csv", newline='', encoding='utf-8') as archivo_entrada:
    lector = csv.DictReader(archivo_entrada)

    for fila in lector:
        año = fila["Año"].strip()
        temporada = fila["Temporada"].strip()
        fecha = fila["Fecha"].strip()

        # Normalizar la fecha
        if fecha == "" or fecha == "0":
            if año.isdigit():
                fecha = f"{año}/12/30"
            else:
                fecha = "0000/00/00"

        clave = (fecha, año, temporada)

        if clave not in fechas_unicas:
            fechas_unicas[clave] = None  # Se usará luego para asignar ID

# Asignamos ID autoincremental a cada fecha única
for idx, clave in enumerate(fechas_unicas.keys(), start=1):
    fechas_unicas[clave] = idx

# Guardamos el archivo final
with open("Fecha.csv", "w", newline='', encoding="utf-8") as archivo_salida:
    campos = ["id_fecha", "fecha", "año", "temporada"]
    escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
    escritor.writeheader()

    for (fecha, año, temporada), id_fecha in fechas_unicas.items():
        escritor.writerow({
            "id_fecha": id_fecha,
            "fecha": fecha,
            "año": año,
            "temporada": temporada
        })

print("✅ Archivo 'Fecha.csv' generado correctamente con fechas únicas e id autoincremental.")
