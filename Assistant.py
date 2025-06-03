from Json_Languages import end_program, supoorted_languages
from SetLenguage import *
from RecognizeLanguage import *
import time
keep_going = True
language = detect_language()


if language:
    speak(language)
    while keep_going:
        command = listen_in_language(language)
        if command:
            speak(language, f"You said: {command}")
            if supoorted_languages(1):
                speak(language, f"{time.strftime("%H:%M:%S")} or {time.strftime("%I:%M:%S")}")
            # if supoorted_languages(2):

        elif end_program() in command:
            keep_going = False
else:
    print("couldn't detect language.")
