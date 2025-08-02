import pyautogui
import webbrowser
import Json_Languages as jl
from urllib.parse import quote


class WebMusicController:
    def __init__(self):
        self.current_service = None
        self.current_tab_url = None

    def play_music_web(self, servicio, busqueda=None):
        servicio_lower = servicio.lower().strip() if servicio else ""

        service_mapping = {
            'youtube': f"https://www.youtube.com/results?search_query={quote(busqueda) if busqueda else ''}",
            'spotify': f"https://open.spotify.com/search/{quote(busqueda) if busqueda else ''}",
            'soundcloud': f"https://soundcloud.com/search?q={quote(busqueda) if busqueda else ''}",
            'apple music': f"https://music.apple.com/search?term={quote(busqueda) if busqueda else ''}",
            'amazon music': f"https://music.amazon.com/search/{quote(busqueda) if busqueda else ''}",
            'deezer': f"https://www.deezer.com/search/{quote(busqueda) if busqueda else ''}",
            'tidal': f"https://tidal.com/search?q={quote(busqueda) if busqueda else ''}"
        }

        for service_key, url in service_mapping.items():
            if service_key in servicio_lower:
                try:
                    webbrowser.open(url)
                    self.current_service = service_key
                    self.current_tab_url = url
                    return f"Abriendo {service_key} {'con búsqueda: ' + busqueda if busqueda else ''}"
                except Exception as e:
                    return f"Error al abrir {service_key}: {e}"

        return f"Servicio '{servicio}' no reconocido"

    def pause_music_universal(self):
        methods = [
            ("Media Key", lambda: pyautogui.press('playpause')),
            ("Spacebar", lambda: pyautogui.press('space')),
            ("K Key", lambda: pyautogui.press('k'))
        ]

        for method_name, method_func in methods:
            try:
                method_func()
                return f"Música pausada/reanudada usando {method_name}"
            except Exception as e:
                continue

        return "No se pudo pausar la música con métodos estándar"

    def pause_spotify(self):
        try:
            pyautogui.press('playpause')
            return "Spotify pausado/reanudado"
        except:
            try:
                pyautogui.press('space')
                return "Spotify pausado con spacebar"
            except:
                return "No se pudo pausar Spotify"

    def pause_soundcloud(self):
        try:
            pyautogui.press('space')
            return "SoundCloud pausado/reanudado"
        except:
            try:
                pyautogui.hotkey('alt', 'shift', 'p')  # Requiere extensión
                return "SoundCloud pausado con atajo"
            except:
                return "No se pudo pausar SoundCloud"

    def pause_apple_music(self):
        try:
            pyautogui.press('playpause')
            return "Apple Music pausado/reanudado"
        except:
            try:
                pyautogui.press('space')
                return "Apple Music pausado con spacebar"
            except:
                return "No se pudo pausar Apple Music"

    def pause_amazon_music(self):
        try:
            pyautogui.press('playpause')
            return "Amazon Music pausado/reanudado"
        except:
            try:
                pyautogui.press('space')
                return "Amazon Music pausado con spacebar"
            except:
                return "No se pudo pausar Amazon Music"

    def pause_deezer(self):
        try:
            pyautogui.press('playpause')
            return "Deezer pausado/reanudado"
        except:
            try:
                pyautogui.press('space')
                return "Deezer pausado con spacebar"
            except:
                return "No se pudo pausar Deezer"

    def pause_tidal(self):
        try:
            pyautogui.press('playpause')
            return "Tidal pausado/reanudado"
        except:
            try:
                pyautogui.press('space')
                return "Tidal pausado con spacebar"
            except:
                return "No se pudo pausar Tidal"

    def pause_current_service(self):
        if not self.current_service:
            return self.pause_music_universal()

        service_methods = {
            'spotify': self.pause_spotify,
            'soundcloud': self.pause_soundcloud,
            'apple music': self.pause_apple_music,
            'amazon music': self.pause_amazon_music,
            'deezer': self.pause_deezer,
            'tidal': self.pause_tidal,
            'youtube': lambda: self.pause_youtube()
        }

        if self.current_service in service_methods:
            return service_methods[self.current_service]()
        else:
            return self.pause_music_universal()

    def pause_youtube(self):
        try:
            pyautogui.press('k')  # YouTube usa 'k' para pause/play
            return "YouTube pausado/reanudado con K"
        except:
            try:
                pyautogui.press('space')
                return "YouTube pausado con spacebar"
            except:
                return "No se pudo pausar YouTube"

    def stop_all_music(self):
        try:
            # Opción 1: Cerrar pestaña actual
            pyautogui.hotkey('ctrl', 'w')
            self.current_service = None
            return "Pestaña de música cerrada"
        except:
            try:
                # Opción 2: Silenciar sistema
                pyautogui.press('volumemute')
                return "Sistema silenciado"
            except:
                return "No se pudo detener la música"

    def volume_control(self, action="mute"):
        volume_commands = {'up':   {"volume up", "turn up volume", "louder", "increase volume", "raise volume"},
                           'down': {"volume down", "turn down volume", "decrease volume", "lower volume", "quieter"},
                           'mute': {"mute", "silence", "quiet", "turn off sound", "mute audio","unmmute","audio","turn on audio","turn on"}
                           }
        try:
            action_lower = action.lower().strip()

            command_type = None
            for cmd_type, keywords in volume_commands.items():
                if any(keyword in action_lower for keyword in keywords):
                    command_type = cmd_type
                    break

            if not command_type: command_type = action_lower
            elif command_type == None: jl.speak("en-US","You didnt say any command volume")

            if command_type == "up":
                pyautogui.press('volumeup')
                return jl.speak("en-US","Volume increased")
            elif command_type == "down":
                pyautogui.press('volumedown')
                return jl.speak("en-US","Volume decreased")
            elif command_type == "mute":
                pyautogui.press('volumemute')
                return jl.speak("en-US","Audio muted/reactivated")
        except Exception as e:
            return f"vollume error: {e}"


music_controller = WebMusicController()

def volume(volume_command):
    return music_controller.volume_control(volume_command)

def play_music_web(services,search):
    return music_controller.play_music_web(services,search)

def pause_web_music():
    return music_controller.pause_current_service()

def stop_web_music():
    return music_controller.stop_all_music()

def play_music_service(service, search=None):
    return music_controller.play_music_web(service, search)

