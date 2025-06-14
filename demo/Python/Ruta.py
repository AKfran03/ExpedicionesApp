import csv

# Leer las rutas únicas del archivo expediciones.csv
rutas_unicas = set()

with open('expediciones.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        ruta = fila['Ruta'].strip()
        if ruta:  # Evitar campos vacíos
            rutas_unicas.add(ruta)

# Ordenamos las rutas para mantener consistencia
rutas_ordenadas = sorted(rutas_unicas)

# Escribir el archivo Ruta.csv
with open('Ruta.csv', 'w', newline='', encoding='utf-8') as f:
    campos = ['id_ruta', 'descripcion']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()

    for idx, ruta in enumerate(rutas_ordenadas, start=1):
        escritor.writerow({'id_ruta': idx, 'descripcion': ruta})

print("✅ Archivo 'Ruta.csv' creado correctamente.")
