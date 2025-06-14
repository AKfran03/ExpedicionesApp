import csv

# Mapeo de motivo_terminacion a id_motivo según tabla dada
motivo_map = {
    "Accidente": 1,
    "Enfermedad, mal de altura, agotamiento o congelación.": 2,
    "Expedicion Completada (subcumbre, antecima)": 3,
    "Expedicion Completada(Pico Principal)": 4,
    "Falta (o pérdida) de suministros, apoyo o equipo": 5,
    "Mal Clima": 6,
    "Otro": 7,
    "Ruta demasiado difícil, falta de experiencia, fuerza o motivación": 8
}

# Leer expediciones.csv
with open('expediciones.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    resultados_unicos = {}
    for fila in lector:
        exito = fila['Exito'].strip()
        motivo = fila['motivo_terminacion'].strip()
        # Evitar filas sin datos
        if exito == '' and motivo == '':
            continue
        # Usamos tupla para evitar duplicados
        key = (exito, motivo)
        if key not in resultados_unicos:
            resultados_unicos[key] = None

# Escribir resultado.csv
with open('resultado.csv', 'w', newline='', encoding='utf-8') as f:
    campos = ['id_resultado', 'descripcion', 'id_motivo']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    id_resultado = 1
    for (exito, motivo) in resultados_unicos:
        id_motivo = motivo_map.get(motivo, None)
        # Si el motivo no está en el mapa, asignamos None o 0
        if id_motivo is None:
            print(f"Advertencia: motivo_terminacion '{motivo}' no encontrado en el mapa. Se asigna id_motivo=0.")
            id_motivo = 0
        escritor.writerow({
            'id_resultado': id_resultado,
            'descripcion': exito,
            'id_motivo': id_motivo
        })
        id_resultado += 1

print("Archivo 'resultado.csv' creado con éxito.")
