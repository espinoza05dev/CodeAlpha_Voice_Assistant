import speech_recognition as sr
import SetLenguage as st
import Json_Languages as jl
import RecognizeLanguage as rl
# 57 languages that can be detected

#has to detect what language the person is speaking
def listening(idioma):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            st.speak()
            audio = r.listen(source)
            comand = r.recognize_google(audio, language=idioma)

    except sr.UnknownValueError:
        st.speak("I did no get that.")
    except sr.RequestError:
        st.speak("Error with request.")


rl.recoglanguage()

comand = listening().strip().lower()

