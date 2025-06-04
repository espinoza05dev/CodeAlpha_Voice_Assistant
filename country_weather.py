import requests

def weather_open_meteo(ciudad_lat, ciudad_lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={ciudad_lat}&longitude={ciudad_lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

    try:
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            current = data['current_weather']
            temp = current['temperature']
            wind = current['windspeed']
            return f"🌡️ {temp}°C, 💨 {wind} km/h"
        else:
            return "Error al obtener el clima"
    except requests.exceptions.RequestException:
        return "Error de conexión"

def get_IP():
    try:
        res = requests.get("http://ip-api.com/json/")
        if res.status_code == 200:
            data = res.json()
            return data.get("city"), data.get("lat"), data.get("lon")
    except:
        pass
    return None, None, None

