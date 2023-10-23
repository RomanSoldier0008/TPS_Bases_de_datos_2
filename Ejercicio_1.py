import pandas as pd
import os
from io import StringIO  # Importa StringIO desde el módulo io

# Directorio donde se encuentran los archivos .txt
directorio = 'clima/'

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Crear un diccionario para almacenar los DataFrames
dataframes = {}

# Leer cada archivo .txt y convertirlo a DataFrame
for archivo in archivos:
    if archivo.endswith('.txt'):
        nombre = archivo.split('.')[0]  # Eliminar la extensión .txt
        ruta_completa = os.path.join(directorio, archivo)
        with open(ruta_completa, 'r') as f:
            contenido = f.read()
        # Utilizar la tabulación como delimitador
        df = pd.read_csv(StringIO(contenido), delimiter='\t')  # Utiliza StringIO directamente
        dataframes[nombre] = df

# Mostrar cada DataFrame en pantalla
for nombre, df in dataframes.items():
    print(f'DataFrame para el archivo: {nombre}')
    print(df)
    print('\n')