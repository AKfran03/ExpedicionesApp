import csv

# Leer valores únicos de "Host"
hosts_unicos = set()

with open("picos.csv", newline='', encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        host = fila["Host"].strip()
        if host:
            hosts_unicos.add(host)

# Ordenar y asignar IDs
hosts_ordenados = sorted(hosts_unicos)
host_id_map = {host: idx + 1 for idx, host in enumerate(hosts_ordenados)}

# Escribir archivo Host.csv
with open("Host.csv", "w", newline='', encoding="utf-8") as archivo_salida:
    campos = ["id_host", "descripcion"]
    escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
    escritor.writeheader()

    for host, id_host in host_id_map.items():
        escritor.writerow({"id_host": id_host, "descripcion": host})

print("✅ Archivo 'Host.csv' generado correctamente.")
