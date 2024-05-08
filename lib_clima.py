# lib_clima.py
import requests

def obtener_clima(ciudad):
    parametros = {
        "q": ciudad,
        "units": "metric",
        "APPID": "1cad6c85a74a33e8aa9dff0eedfc3347"
    }
    respuesta = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=parametros)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        clima_info = {
            'temperatura': datos["main"]["temp"],
            'humedad': datos["main"]["humidity"],
            'ciudad': datos["name"]
        }
        return clima_info
    else:
        return None
