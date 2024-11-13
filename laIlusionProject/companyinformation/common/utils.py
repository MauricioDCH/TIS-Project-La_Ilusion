from django.core.cache import cache
import requests

from django.core.cache import cache
import requests
from datetime import datetime, timezone, timedelta

def get_cached_api_data():
    # Verifica si los datos están en caché
    data = cache.get('api_data')
    
    if not data:
        # Realiza el llamado a la API y obtiene los datos completos
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=6.25184&lon=-75.56359&appid=7a4dbe3c6f7c463002172edafeaf5afc')
        
        if response.status_code == 200:
            full_data = response.json()
            
            # Filtra solo los datos necesarios con un manejo de errores
            timestamp = full_data.get("dt", None)
            if timestamp:
                # Convierte el timestamp de UTC a tu zona horaria
                utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                local_time = utc_time.astimezone(timezone(timedelta(hours=-5)))  # UTC-5 para la hora de Colombia
                data_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
            else:
                data_time = "Hora no disponible"
            
            data = {
                "city": full_data.get("name", "Ciudad no disponible"),
                "country": full_data.get("sys", {}).get("country", "País no disponible"),
                "temperature": full_data.get("main", {}).get("temp", "Temperatura no disponible"),
                "description": full_data.get("weather", [{}])[0].get("description", "Descripción no disponible"),
                "humidity": full_data.get("main", {}).get("humidity", "Humedad no disponible"),
                "wind_speed": full_data.get("wind", {}).get("speed", "Velocidad de viento no disponible"),
                "data_time": data_time,
            }
            
            # Cachea los datos durante 15 minutos (900 segundos)
            cache.set('api_data', data, timeout=900)
        else:
            # Si falla el llamado a la API, devuelve valores predeterminados
            data = {
                "city": "Ciudad no disponible",
                "country": "País no disponible",
                "temperature": "Temperatura no disponible",
                "description": "Descripción no disponible",
                "humidity": "Humedad no disponible",
                "wind_speed": "Velocidad de viento no disponible",
                "data_time": "Hora no disponible",
            }
    
    return data

