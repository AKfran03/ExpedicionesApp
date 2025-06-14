import csv

def cargar_diccionario(archivo, key_col, val_col, val_col2=None):
    d = {}
    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            key = fila[key_col].strip()
            if val_col2:
                d[key] = (int(fila[val_col]), int(fila[val_col2]))
            else:
                d[key] = int(fila[val_col])
    return d

def cargar_diccionario_descripcion_id(archivo, id_col, desc_col):
    d = {}
    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            d[fila[desc_col].strip()] = int(fila[id_col])
    return d

def cargar_resultado_con_motivo(resultado_file, motivo_file):
    # Carga Motivo.csv para mapear id_motivo → descripcion_motivo
    motivo_id_to_desc = {}
    with open(motivo_file, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            motivo_id_to_desc[int(fila['id_motivo'])] = fila['descripcion'].strip()

    # Carga Resultado.csv con relacion a Motivo.csv
    resultado = {}
    with open(resultado_file, newline='', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            desc = fila['descripcion'].strip()
            id_resultado = int(fila['id_resultado'])
            id_motivo = int(fila['id_motivo'])
            motivo_desc = motivo_id_to_desc.get(id_motivo, None)
            resultado[(desc, motivo_desc)] = id_resultado

    return resultado

def convertir_bit_si_no(valor):
    v = valor.strip().lower().replace("í","i")
    return 1 if v == "si" else 0

# Cargo Fecha.csv: fecha → id_fecha
fecha_dict = cargar_diccionario_descripcion_id('Fecha.csv', 'id_fecha', 'fecha')

# Cargo Accidente.csv: descripcion → id_accidente
accidente_dict = cargar_diccionario_descripcion_id('Accidente.csv', 'id_accidente', 'descripcion')

# Cargo Ruta.csv: descripcion → id_ruta
ruta_dict = cargar_diccionario_descripcion_id('Ruta.csv', 'id_ruta', 'descripcion')

# Cargo Motivo.csv y Resultado.csv (con enlace)
resultado_dict = cargar_resultado_con_motivo('Resultado.csv', 'Motivo.csv')

# Cargo Miembros.csv: índice por id_expedicion (muchos miembros por expedición)
miembros_por_expedicion = {}
with open('Mieembros.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        id_exp = fila['id_expedicion'].strip()
        if id_exp not in miembros_por_expedicion:
            miembros_por_expedicion[id_exp] = []
        miembros_por_expedicion[id_exp].append(int(fila['id_miembro']))

# Cargo Picos.csv: índice codigo_pico → id_pico
codigo_pico_a_id = {}
with open('Piicos.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        codigo_pico = fila['codigo_pico'].strip()
        codigo_pico_a_id[codigo_pico] = int(fila['id_pico'])

# Ahora proceso Expediciones.csv
with open('Expediciones.csv', newline='', encoding='utf-8') as f_entrada, \
     open('Expediciones_final.csv', 'w', newline='', encoding='utf-8') as f_salida:

    lector = csv.DictReader(f_entrada)
    campos = [
        'id_expedicion', 'id_fecha', 'id_accidente', 'id_miembro',
        'id_pico', 'id_resultado', 'id_ruta',
        'altitud', 'cupos', 'conteo_mortalidad'
    ]
    escritor = csv.DictWriter(f_salida, fieldnames=campos)
    escritor.writeheader()

    id_expedicion_auto = 1

    for fila in lector:
        # Datos para buscar
        fecha = fila['Fecha'].strip()
        accidente = fila['Accidente'].strip()
        id_exp_original = fila['id_expedicion'].strip()
        codigo_pico = fila['codigo_pico'].strip()
        exito = fila['Exito'].strip()
        motivo = fila['motivo_terminacion'].strip()
        ruta = fila['Ruta'].strip()

        # id_fecha
        id_fecha = fecha_dict.get(fecha)
        if id_fecha is None:
            print(f"⚠ Fecha no encontrada: {fecha}")
            continue

        # id_accidente
        id_accidente = accidente_dict.get(accidente)
        if id_accidente is None:
            print(f"⚠ Accidente no encontrado: {accidente}")
            continue

        # id_ruta
        id_ruta = ruta_dict.get(ruta)
        if id_ruta is None:
            print(f"⚠ Ruta no encontrada: {ruta}")
            continue

        # id_pico
        id_pico = codigo_pico_a_id.get(codigo_pico)
        if id_pico is None:
            print(f"⚠ Pico no encontrado: {codigo_pico}")
            continue

        # id_resultado
        # Buscamos id_resultado por el par (Exito, motivo_terminacion)
        id_resultado = None
        # Para buscar, necesitamos el texto del motivo_terminacion que corresponde al id_motivo
        # Pero en resultado_dict la key es (descripcion, motivo_descripcion)
        # Vamos a intentar buscar con el motivo_terminacion de Motivo.csv (descripción)
        # Pero nosotros solo tenemos motivo_terminacion (texto), que debe coincidir con descripcion en Motivo.csv
        # Entonces, para encontrar motivo_desc, vamos a buscar en Motivo.csv qué id tiene motivo_terminacion y luego su descripcion
        # Pero ya tenemos esa tabla resultado_dict que tiene (resultado_desc, motivo_desc) -> id_resultado

        # Lo mejor es revertir motivo_dict para buscar motivo_desc de motivo_terminacion:
        # Leemos Motivo.csv otra vez para obtener dict descripcion->id_motivo
        motivo_desc_to_id = {}
        with open('Motivo.csv', newline='', encoding='utf-8') as f_motivo:
            lector_m = csv.DictReader(f_motivo)
            for mrow in lector_m:
                motivo_desc_to_id[mrow['descripcion'].strip()] = int(mrow['id_motivo'])

        id_motivo = motivo_desc_to_id.get(motivo)
        if id_motivo is None:
            print(f"⚠ Motivo no encontrado: {motivo}")
            continue

        # Ahora buscamos el motivo_desc que tenga id_motivo, leyendo Motivo.csv (ya lo tenemos en motivo_id_to_desc)
        # Ya que cargamos antes motivo_id_to_desc en la función cargar_resultado_con_motivo, pero no lo guardamos global, volvemos a cargarlo:

        motivo_id_to_desc = {}
        with open('Motivo.csv', newline='', encoding='utf-8') as f_motivo:
            lector_m = csv.DictReader(f_motivo)
            for mrow in lector_m:
                motivo_id_to_desc[int(mrow['id_motivo'])] = mrow['descripcion'].strip()

        motivo_desc = motivo_id_to_desc.get(id_motivo)

        id_resultado = resultado_dict.get((exito, motivo_desc))
        if id_resultado is None:
            print(f"⚠ Resultado no encontrado para exito='{exito}', motivo='{motivo_desc}'")
            continue

        # Encontrar todos los miembros para esta expedición
        miembros = miembros_por_expedicion.get(id_exp_original)
        if miembros is None:
            print(f"⚠ Miembros no encontrados para expedicion: {id_exp_original}")
            continue

        # Valores que se repiten para cada miembro
        altitud = int(fila['altitud']) if fila['altitud'].isdigit() else 0
        cupos = int(fila['cupo']) if fila['cupo'].isdigit() else 0
        conteo_mortalidad = int(fila['Muertes']) if fila['Muertes'].isdigit() else 0

        # Por cada miembro escribir una fila
        for id_miembro in miembros:
            escritor.writerow({
                'id_expedicion': id_expedicion_auto,
                'id_fecha': id_fecha,
                'id_accidente': id_accidente,
                'id_miembro': id_miembro,
                'id_pico': id_pico,
                'id_resultado': id_resultado,
                'id_ruta': id_ruta,
                'altitud': altitud,
                'cupos': cupos,
                'conteo_mortalidad': conteo_mortalidad
            })

            id_expedicion_auto += 1

print("✅ Expediciones_final.csv creado correctamente.")
