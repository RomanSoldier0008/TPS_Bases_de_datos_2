import requests
import pandas as pd

# URL de la API de Pageviews de Wikimedia para Albert Einstein en Wikipedia
url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/Albert_Einstein/daily/2023/01/01/2023/12/31"

# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir los datos JSON en un DataFrame
    data = response.json()
    df = pd.DataFrame(data['items'])
    
    # Mostrar el DataFrame en pantalla
    print(df)
else:
    print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")