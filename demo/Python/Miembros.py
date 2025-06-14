import csv

# Cargar nacionalidades: descripcion → id_nacionalidad
nacionalidades = {}
with open('nacionalidad.csv', newline='', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        desc = fila['descripcion'].strip()
        nacionalidades[desc] = int(fila['id_nacionalidad'])

# Función para convertir "Sí"/"No" (con o sin tilde) a bit
def convertir_bit(valor):
    valor = valor.strip().lower().replace("í", "i")
    return 1 if valor == "si" else 0

# Leer miembros.csv y generar Mieembros.csv con id_miembro autoincremental
with open('miembros.csv', newline='', encoding='utf-8') as f_entrada, \
     open('Mieembros.csv', 'w', newline='', encoding='utf-8') as f_salida:
    
    lector = csv.DictReader(f_entrada)
    campos = ['id_miembro', 'id_nacionalidad', 'nombre', 'apellido', 'sexo', 'es_lider', 'es_staff', 'año_nacimiento', 'fallecido', 'id_expedicion']
    escritor = csv.DictWriter(f_salida, fieldnames=campos)
    escritor.writeheader()

    id_auto = 1
    for fila in lector:
        nacionalidad = fila['nacionalidad'].strip()
        if nacionalidad not in nacionalidades:
            print(f"⚠ Nacionalidad no encontrada: {nacionalidad}")
            continue

        escritor.writerow({
            'id_miembro': id_auto,
            'id_nacionalidad': nacionalidades[nacionalidad],
            'nombre': fila['nombre'].strip(),
            'apellido': fila['apellido'].strip(),
            'sexo': fila['sexo'].strip(),
            'es_lider': convertir_bit(fila['es_lider']),
            'es_staff': convertir_bit(fila['contratado']),
            'año_nacimiento': int(fila['año_nacimiento']),
            'fallecido': convertir_bit(fila['fallecido']),
            'id_expedicion': fila['id_expedicion'].strip()
        })

        id_auto += 1

print("✅ Archivo 'Mieembros.csv' creado correctamente.")
