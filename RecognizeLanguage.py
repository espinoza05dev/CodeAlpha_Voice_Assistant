from logging import exception
import speech_recognition as sr
from langdetect import detect

r = sr.Recognizer()

def recoglanguage():
    with sr.Microphone() as source:
        print("You need to Speak to detect any laguage...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)

        detected_language = detect(text)
        return detected_language
    except exception as i:
        print(f"there was an issue: {i}")
    except sr.UnknownValueError:
        print("it was not understood.")
    except sr.RequestError as e:
        print(f"Error al conectar con el servicio: {e}")