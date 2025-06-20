import csv

# Paso 1: Cargar miembros y verificar quién es líder
lideres = set()
with open('Miembros.csv', newline='', encoding='utf-8') as f_miembros:
    lector_miembros = csv.DictReader(f_miembros)
    for fila in lector_miembros:
        if fila['es_lider'].strip() == '1':
            lideres.add(fila['id_miembro'].strip())

# Paso 2: Procesar expediciones
with open('Expediciones.csv', newline='', encoding='utf-8') as f_expediciones, \
     open('Expediciones_filtrado.csv', 'w', newline='', encoding='utf-8') as f_salida:

    lector_expediciones = csv.DictReader(f_expediciones)
    campos = lector_expediciones.fieldnames
    escritor = csv.DictWriter(f_salida, fieldnames=campos)
    escritor.writeheader()

    for fila in lector_expediciones:
        id_miembro = fila['id_miembro'].strip()
        if id_miembro not in lideres:
            fila['altitud'] = '0'
            fila['cupos'] = '0'
            fila['conteo_mortalidad'] = '0'
        escritor.writerow(fila)

print("✅ Expediciones_filtrado.csv creado correctamente. Datos numéricos solo en líderes.")
