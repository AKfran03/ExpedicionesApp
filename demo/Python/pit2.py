import csv

# Abrimos el archivo original
with open("expediciones.csv", newline='', encoding='utf-8') as archivo_entrada:
    lector = csv.DictReader(archivo_entrada)
    filas_corregidas = []

    for fila in lector:
        fecha = fila["Fecha"].strip()
        año = fila["Año"].strip()

        # Si la fecha está vacía o es "0", la corregimos
        if fecha == "" or fecha == "0":
            if año.isdigit():
                fila["Fecha"] = f"{año}/12/30"
            else:
                fila["Fecha"] = "0000/00/00"  # Fallback si no hay año válido

        filas_corregidas.append(fila)

# Escribimos el nuevo archivo corregido
with open("expediciones_corregido.csv", "w", newline='', encoding='utf-8') as archivo_salida:
    campos = lector.fieldnames
    escritor = csv.DictWriter(archivo_salida, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(filas_corregidas)

print("✅ Archivo corregido guardado como 'expediciones_corregido.csv'")
