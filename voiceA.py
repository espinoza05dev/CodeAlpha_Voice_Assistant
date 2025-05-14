import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def cambiar_voz(idioma="en"):
    voces = engine.getProperty('voices')
    for voz in voces:
        if idioma == "es" and "spanish" in voz.name.lower():
            engine.setProperty('voice', voz.id)
            return
        elif idioma == "en" and "english" in voz.name.lower():
            engine.setProperty('voice', voz.id)
            return

def hablar(texto, idioma="en"):
    cambiar_voz(idioma)
    engine.say(texto)
    engine.runAndWait()

def escuchar(idioma="en-EN"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language=idioma)
            print(f"You Said: {comando}")
            return comando.lower()
        except sr.UnknownValueError:
            print("I didn't get that.")
            return ""
        except sr.RequestError:
            print("Error with request.")
            return ""


hablar("¿What language do you want?")
comando =  escuchar().strip().lower()

if "english" or "ingles" in comando:
    lang_code = "en-US"
    hablar("Hi, I'm your assistant. How can I help you?", "en")
else:
    lang_code = "es-ES"
    hablar("Hola, soy tu asistente. ¿En qué puedo ayudarte?", "es")


# #comando = escuchar(lang_code)
# if  :
#     if "time" in comando:
#         hora = datetime.now().strftime("%I:%M %p")
#         hablar(f"The time is {hora}", "en")
# else:
#     if "hora" in comando or "ahora" in comando:
#         hora = datetime.now().strftime("%I:%M %p").replace("AM", "a. m.").replace("PM", "p. m.")
#         hablar(f"Son las {hora}", "es")
