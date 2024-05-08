
API_key = "1cad6c85a74a33e8aa9dff0eedfc3347"
#https://api.openweathermap.org/data/2.5/weather?lat=25.6866&lon=100.3161&appid=1cad6c85a74a33e8aa9dff0eedfc3347

import requests
# Pedimos el nombre de la ciudad por teclado
ciudad=input("Dime el nombre de una ciudad:")
# Creamos un diccionario con los parámetros de la URL
parametros={"q":ciudad,
            "units":"metric",
            "APPID":"1cad6c85a74a33e8aa9dff0eedfc3347"}
# Realizamos la petición, indicando la URL y los parámetros
respuesta=requests.get("http://api.openweathermap.org/data/2.5/weather",params=parametros)
# Si la respuesta devuelve el código de estado 200, todo ha ido bien
if respuesta.status_code == 200:
    # La respuesta json se convierte en un diccionario
    datos = respuesta.json()
    # Se obtienen los valores del diccionario
    print("La temperatura actual es:",datos["main"]["temp"],"ºC")
    print("La sensación térmica es:",datos["main"]["feels_like"],"ºC")
    print("La temperatura mínima es:",datos["main"]["temp_min"],"ºC")
    print("La temperatura máxima es:",datos["main"]["temp_max"],"ºC")
    print("La presión es:",datos["main"]["pressure"],"hPa")
    print("La humedad es:",datos["main"]["humidity"],"%")
else:
    print("De esa ciudad no tengo datos.")