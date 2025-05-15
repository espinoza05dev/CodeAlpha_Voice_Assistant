from logging import exception
import speech_recognition as sr
from langdetect import detect

r = sr.Recognizer()

def recoglanguage():
    with sr.Microphone() as source:
        print("Habla algo para detectar el idioma...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio)

        idioma_detectado = detect(texto)
        print("Idioma detectado:", idioma_detectado)

    except exception as i:
        print(f"hubo un error: {i}")
    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
    except sr.RequestError as e:
        print(f"Error al conectar con el servicio: {e}")