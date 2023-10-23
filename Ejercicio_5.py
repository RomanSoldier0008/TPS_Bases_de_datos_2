import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página de Wikipedia con la tabla de ciudades más pobladas de Argentina
url = "https://es.wikipedia.org/wiki/Anexo:Ciudades_de_Argentina_por_poblaci%C3%B3n"

# Realizar la solicitud HTTP a la página web
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Crear un objeto BeautifulSoup para analizar la página web
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar la tabla que contiene la información (ajusta esto según la estructura de la página)
    table = soup.find('table', {'class': 'wikitable'})
    
    # Extraer datos de la tabla y almacenarlos en una lista de listas
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all(['td', 'th'])  # Ajusta según las etiquetas que contienen los datos
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(data)
    
    # Mostrar el DataFrame en pantalla
    print(df)
else:
    print(f"Error en la solicitud a la página web. Código de estado: {response.status_code}")