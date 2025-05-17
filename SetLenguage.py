import pyttsx3
engine = pyttsx3.init()

def change_voice(language):
    voice = engine.getProperty('voices')
    for voz in voice:
        if language in voz.name.lower():
            engine.setProperty('voice', voz.id)
            return

def speak(language,text = ""):
    change_voice(language)
    engine.say(text)
    engine.runAndWait()
