import os
import subprocess
import webbrowser
from urllib.parse import quote

def reproducir_audio_pygame(archivo):
    """Reproduce audio usando pygame"""
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()
        return f"Reproduciendo {archivo} con pygame"
    except ImportError:
        return "Instala pygame: pip install pygame"
    except Exception as e:
        return f"Error: {e}"

def descargar_youtube_audio(url, carpeta_destino="./musica/"):
    """Descarga audio de YouTube (requiere yt-dlp)"""
    try:
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Comando para yt-dlp
        comando = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "192K",
            "-o", f"{carpeta_destino}%(title)s.%(ext)s",
            url
        ]

        resultado = subprocess.run(comando, capture_output=True, text=True)
        if resultado.returncode == 0:
            return f"Audio descargado exitosamente en {carpeta_destino}"
        else:
            return f"Error: {resultado.stderr}"
    except FileNotFoundError:
        return "Instala yt-dlp: pip install yt-dlp"

def vlc_control(archivo_musica=None, accion="play"):
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Ruta típica en Windows

    if archivo_musica:
        if os.path.exists(vlc_path):
            subprocess.Popen([vlc_path, archivo_musica])
            return f"Reproduciendo {archivo_musica} en VLC"
        else:
            return "VLC no encontrado. Instala VLC Media Player"
    else:
        return "Especifica un archivo de música"

def windows_media_player(archivo_musica):
    if os.name == 'nt' and archivo_musica:
        os.startfile(archivo_musica)
        return f"Reproduciendo {archivo_musica}"
    return "Solo funciona en Windows"

def reproductor_inteligente(busqueda, modo="web"):

    if modo == "web":
        # Buscar en YouTube
        url_youtube = f"https://www.youtube.com/results?search_query={quote(busqueda + ' audio')}"
        webbrowser.open(url_youtube)
        return f"🔍 Buscando '{busqueda}' en YouTube"

    elif modo == "local":
        # Buscar archivos locales
        extensiones = ['.mp3', '.wav', '.flac', '.m4a', '.ogg']
        carpetas_musica = [
            os.path.expanduser("~/Music"),
            os.path.expanduser("~/Downloads"),
            "./musica/"
        ]

        for carpeta in carpetas_musica:
            if os.path.exists(carpeta):
                for archivo in os.listdir(carpeta):
                    if any(archivo.lower().endswith(ext) for ext in extensiones):
                        if busqueda.lower() in archivo.lower():
                            archivo_completo = os.path.join(carpeta, archivo)
                            return reproducir_audio_pygame(archivo_completo)

        return f"❌ No se encontró '{busqueda}' en archivos locales"

    elif modo == "descargar":
        # Buscar en YouTube y descargar
        url_busqueda = f"ytsearch:\"{busqueda}\""
        return descargar_youtube_audio(url_busqueda)


def play_music_web(servicio, busqueda=None):
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

    url_to_open = None
    service_name = None

    for service_key, url in service_mapping.items():
        if service_key in servicio_lower:
            url_to_open = url
            service_name = service_key
            break

    if url_to_open:
        try:
            webbrowser.open(url_to_open)
            return f"Abriendo {service_name} {'con búsqueda: ' + busqueda if busqueda else ''}"
        except Exception as e:
            return f"Error al abrir {service_name}: {e}"
    else:
        available_services = list(service_mapping.keys())
        return f"Servicio '{servicio}' no reconocido. Servicios disponibles: {', '.join(available_services)}"

