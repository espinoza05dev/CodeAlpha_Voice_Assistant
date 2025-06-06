import json
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


with open("basic_commands.json", "r", encoding="utf-8") as f:
    data = json.load(f)

COMMANDS = { 1: "time", 2: "weather", 3: "music", 4: "stop_music", 5: "volume",
             6: "search", 7: "hello", 8: "help", 9: "joke", 10: "exit"
             }

def commands_voice(cmd):
    if cmd in COMMANDS: return " ".join(data["basic_voice_commands"][COMMANDS[cmd]]["keywords"])
    return ""

def response_voice(cmd):
    if cmd in COMMANDS: return "".join(data["basic_voice_commands"][COMMANDS[cmd]]["response"])
    return ""