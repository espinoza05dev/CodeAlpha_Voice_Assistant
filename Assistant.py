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
        speak(language,"Say something")
        while keep_going:
            command = listen_in_language(language)
            if command:
                speak(language, f"You said: {command}")

                #time
                if command in commands_voice(1):
                    speak(language, response_voice(1))
                    time.sleep(2)
                    speak(language, f"{time.strftime("%H:%M:%S")} or {time.strftime("%I:%M:%S")}")

                #weather
                if command in commands_voice(2):
                    speak(language, response_voice(2))
                    if city and lat and lon: speak(language, f"City: {city}, weather:{weather_open_meteo(lat, lon)}")
                else:
                    speak("I could not get the weather")

                #music
                if command in commands_voice(3):
                    speak(language, "Where do you want to play music?")
                    services = listen_in_language(language)
                    speak(language, f"You said {services}")

                    available_services = ["youtube", "spotify", "soundcloud", "apple music", "amazon music", "deezer",
                                          "tidal"]

                    services_lower = services.lower() if services else ""

                    service_found = any(service in services_lower for service in available_services)

                    if service_found:
                        speak(language, "What music would you like to play?")
                        search = listen_in_language(language)
                        speak(language, f"You said {search}")

                        if search and search.strip():
                            play_music_web(services, search)
                        else:
                            speak(language, "I didn't catch what music you want to play")
                    else:
                        speak(language, "No service available or recognized")

                #stop music
                if command in commands_voice(4):
                    # speak(language, response_voice(4))
                    print()

                #volume
                if command in commands_voice(5):
                    speak(language, response_voice(5))
                    print()

                #search
                if command in commands_voice(6):
                    speak(language, response_voice(6))
                    print()

                #hello
                if command in commands_voice(7):
                    speak(language, response_voice(7))


                #help
                if command in commands_voice(8):
                    speak(language, response_voice(8))

                #joke
                if command in commands_voice(9):
                    speak(language, response_voice(9))
                    print()

                #exit
                if command in commands_voice(10):
                    speak(language, response_voice(10))
                    keep_going = False
                else:
                    continue
except Exception as e:
    print(f"there was an issue: {e}")
