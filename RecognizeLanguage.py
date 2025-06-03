import speech_recognition as sr

def detect_language():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="en-US")
        return command
    except sr.UnknownValueError as u:
        print(f"there was an issue {u}")
    except sr.RequestError as e:
        print(f"Error while trying to connect the service: {e}")

    print("Language could not be recognized.")
    return None


def listen_in_language(language):
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        command = r.recognize_google(audio, language=language)
        return command
    except sr.UnknownValueError:
        print(".")
    except sr.RequestError as e:
        print(f"Error al conectar con el servicio: {e}")
    return None
