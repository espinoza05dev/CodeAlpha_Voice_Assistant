import sys
from logging import exception
import speech_recognition as sr
import Json_Languages
import SetLenguage

#detect what language the person is speaking
# 57 languages that can be detected
def listening(languages):
#in case there is any issue the try
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        SetLenguage.speak("Say something...")
        comand = r.recognize_google(audio,language=languages)

        exit_program = comand.lower()

        if exit_program in Json_Languages.supoorted_languages():
            sys.exit()

    except exception as i:
        print(f"there was an issue: {i}")
    except sr.UnknownValueError:
        print("it was not understood.")
    except sr.RequestError as e:
        print(f"Error al conectar con el servicio: {e}")

