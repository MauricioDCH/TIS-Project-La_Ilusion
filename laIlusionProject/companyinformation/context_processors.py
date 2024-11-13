
from .common.utils import get_cached_api_data  # Importa tu función de caché o utilidades

def weather_data(request):
    # Obtén los datos de la API, en este caso desde la función de caché
    data = get_cached_api_data()
    return {'weather_data': data}