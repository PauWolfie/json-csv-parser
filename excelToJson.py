import os
import pandas as pd
import json

# Nombre de la carpeta que contiene los archivos Excel
carpeta_csv = 'csv'

# Nombre de la carpeta donde se guardarán los archivos JSON
carpeta_json = 'json'

# Asegurarse de que la carpeta de salida exista
if not os.path.exists(carpeta_json):
    os.makedirs(carpeta_json)

# Iterar sobre los archivos en la carpeta 'csv'
for archivo_csv in os.listdir(carpeta_csv):
    if archivo_csv.endswith('.xlsx'):
        ruta_csv = os.path.join(carpeta_csv, archivo_csv)

        # Leer el archivo Excel
        df = pd.read_excel(ruta_csv)

        # Convertir el DataFrame a un diccionario personalizado
        data_dict = dict(zip(df['Nombre_Columna_Indice'], df['Valor']))

        # Construir la ruta para el archivo JSON de salida en la carpeta 'json'
        ruta_json = os.path.join(carpeta_json, os.path.splitext(archivo_csv)[0] + '.json')

        # Escribir el diccionario a un archivo JSON
        with open(ruta_json, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, indent=2, ensure_ascii=False)

print("La conversión de Excel a JSON ha sido completada.")
