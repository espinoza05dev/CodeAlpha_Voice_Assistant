from Json_Languages import *
from SetLenguage import *
from RecognizeLanguage import *
from country_weather import *
from music import *
import time

try:
    city, lat, lon = get_IP()
    language = detect_language()
    keep_going = True

    if language:
        speak(language)
        while keep_going:
            command = listen_in_language(language)
            if command:
                speak(language, f"You said: {command}")

                if command in commads_voice(1):
                    speak(language, response_voice(1))
                    time.sleep(2)
                    speak(language, f"{time.strftime("%H:%M:%S")} or {time.strftime("%I:%M:%S")}")

                if command in commads_voice(2):
                    speak(language, response_voice(2))
                    if city and lat and lon: speak(language, f"City: {city}, weather:{weather_open_meteo(lat, lon)}")
                else:
                    speak("I could not get the weather")

                if command in commads_voice(3):
                    speak(language, response_voice(3))
                    abrir_reproductor_web()
                if command in commads_voice(4):
                    speak(language, response_voice(4))
                    print()
                if command in commads_voice(5):
                    speak(language, response_voice(5))
                    print()
                if command in commads_voice(6):
                    speak(language, response_voice(6))
                    print()
                if command in commads_voice(7):
                    speak(language, response_voice(7))

                if command in commads_voice(8):
                    speak(language, response_voice(8))
                if command in commads_voice(9):
                    speak(language, response_voice(9))
                    print()

                if command in commads_voice(10):
                    speak(language, response_voice(10))
                    keep_going = False
                else:
                    continue
except Exception as e:
    print(f"there was an issue: {e}")
