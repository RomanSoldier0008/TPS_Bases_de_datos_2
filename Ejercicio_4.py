import requests
import pandas as pd

# URL de la API Nager.Date para obtener las fiestas nacionales argentinas en 2021
url = "https://date.nager.at/Api/v2/PublicHoliday/2021/ar"

# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir los datos JSON en un DataFrame
    data = response.json()
    df = pd.DataFrame(data)
    
    # Mostrar el DataFrame en pantalla
    print(df)
else:
    print(f"Error en la solicitud a la API. Código de estado: {response.status_code}")