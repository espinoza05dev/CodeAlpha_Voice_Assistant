from Json_Languages import *
from RecognizeLanguage import *
from country_weather import *
from music import *
from searches import *
import time

language = detect_language()

try:
    city, lat, lon = get_IP()
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
                    pause_web_music()
                    speak(language, response_voice(4))

                #volume
                if command in commands_voice(5):
                    volume_command = listen_in_language(language)
                    speak(language, f"You said {volume_command}")
                    volume(volume_command)

                #search
                if command in commands_voice(6):
                    speak(language, response_voice(6))

                    search_query = listen_in_language(language)
                    speak(language, f"You want to search for: {search_query}")

                    if search_query and search_query.strip():
                        available_browsers = browser_controller.get_available_browsers()

                        if len(available_browsers) > 1:
                            speak(language,
                                  f"Which browser? Available: {', '.join(available_browsers)}, or say 'default'")
                            browser_choice = listen_in_language(language)

                            browser_to_use = None
                            if browser_choice:
                                browser_lower = browser_choice.lower()
                                for browser in available_browsers:
                                    if browser in browser_lower:
                                        browser_to_use = browser
                                        break
                        else:
                            browser_to_use = None

                        search_engine = "google"  # por defecto
                        if search_query:
                            query_lower = search_query.lower()
                            if "bing" in query_lower:
                                search_engine = "bing"
                                search_query = search_query.replace("bing", "").strip()
                            elif "duckduckgo" in query_lower or "duck duck go" in query_lower:
                                search_engine = "duckduckgo"
                                search_query = search_query.replace("duckduckgo", "").replace("duck duck go",
                                                                                              "").strip()
                            elif "yahoo" in query_lower:
                                search_engine = "yahoo"
                                search_query = search_query.replace("yahoo", "").strip()

                        result = browser_controller.search_with_browser(browser_to_use, search_query, search_engine)
                        speak(language, result)
                    else:
                        speak(language, "I didn't catch what you want to search for")

            if "search youtube" in command.lower() or "youtube search" in command.lower():
                speak(language, "What do you want to search on YouTube?")
                query = listen_in_language(language)
                if query:
                    result = browser_controller.search_youtube(query)
                    speak(language, result)

            if "search wikipedia" in command.lower() or "wikipedia search" in command.lower():
                speak(language, "What do you want to search on Wikipedia?")
                query = listen_in_language(language)
                if query:
                    result = browser_controller.search_wikipedia(query)
                    speak(language, result)

            if "open facebook" in command.lower():
                result = browser_controller.open_social_media("facebook")
                speak(language, result)
            elif "open twitter" in command.lower():
                result = browser_controller.open_social_media("twitter")
                speak(language, result)
            elif "open instagram" in command.lower():
                result = browser_controller.open_social_media("instagram")
                speak(language, result)

            if "open browser" in command.lower():
                available_browsers = browser_controller.get_available_browsers()

                browser_to_open = None
                command_lower = command.lower()

                for browser in available_browsers:
                    if browser in command_lower:
                        browser_to_open = browser
                        break

                result = browser_controller.open_browser(browser_to_open)
                speak(language, result)

                #hello
                if command in commands_voice(7):
                    speak(language, response_voice(7))

                #help
                if command in commands_voice(8):
                    speak(language, response_voice(8))

                #joke
                if command in commands_voice(9):
                    speak(language, response_voice(9))
                    #poner alguna broma

                #exit
                if command in commands_voice(10):
                    speak(language, response_voice(10))
                    keep_going = False
                else:
                    continue
except Exception as e:
    speak(language,"there was an issue")
    print(f"the issue: {e}")
