from Json_Languages import end_program, supoorted_languages
from SetLenguage import *
from RecognizeLanguage import *
import time
from country_weather import *

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

                if command in supoorted_languages(1): speak(language,f"{time.strftime("%H:%M:%S")} or {time.strftime("%I:%M:%S")}")

                if command in supoorted_languages(2):
                    if city and lat and lon: speak(language, f"City: {city}, weather:{weather_open_meteo(lat, lon)}")
                else:
                    speak("I could not get the weather")

                if command in supoorted_languages(3): print()

                if command in end_program(): keep_going = False
                else: continue

    else:
        print("couldn't detect language.")
except Exception as e:
    print(f"there was an issue: {e}")