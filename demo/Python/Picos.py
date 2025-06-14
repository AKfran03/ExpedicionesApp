import csv

# Cargar Localizacion.csv: descripcion → id_localizacion
localizaciones = {}
with open('Localizacion.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        desc = fila['descripcion'].strip()
        localizaciones[desc] = int(fila['id_localizacion'])

# Crear Piicos.csv
with open('picos.csv', newline='', encoding='utf-8') as f_entrada, \
     open('Piicos.csv', 'w', newline='', encoding='utf-8') as f_salida:

    lector = csv.DictReader(f_entrada)
    campos = [
        'id_pico', 'id_localizacion', 'abierto', 'altura',
        'cambio_trekking', 'sin_aprobacion', 'año_de_cambio',
        'estado', 'restricciones', 'codigo_pico'
    ]
    escritor = csv.DictWriter(f_salida, fieldnames=campos)
    escritor.writeheader()

    def convertir_bit(valor):
        return 1 if valor.strip().upper() == "SI" else 0

    id_auto = 1
    for fila in lector:
        loc = fila['Localizacion'].strip()
        if loc not in localizaciones:
            print(f"⚠ Localización no encontrada: {loc}")
            continue

        escritor.writerow({
            'id_pico': id_auto,
            'id_localizacion': localizaciones[loc],
            'abierto': convertir_bit(fila['Abierto']),
            'altura': int(fila['Altura'].strip()),
            'cambio_trekking': convertir_bit(fila['cambio_a_trekking']),
            'sin_aprobacion': convertir_bit(fila['Sin_aprobacion']),
            'año_de_cambio': int(fila['Año_De_Cambio'].strip()) if fila['Año_De_Cambio'].strip().isdigit() else 0,
            'estado': fila['Estado'].strip(),
            'restricciones': fila['Restriccion'].strip(),
            'codigo_pico': fila['codigo_pico'].strip()
        })

        id_auto += 1

print("✅ Piicos.csv creado correctamente con valores binarios convertidos y codigo_pico agregado.")
