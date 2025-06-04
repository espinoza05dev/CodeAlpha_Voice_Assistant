import os
import subprocess
import webbrowser
from urllib.parse import quote

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

def windows_media_player(archivo_musica):
    """Abre Windows Media Player"""
    if os.name == 'nt' and archivo_musica:
        os.startfile(archivo_musica)
        return f"Reproduciendo {archivo_musica}"
    return "Solo funciona en Windows"

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

def reproductor_inteligente(busqueda, modo="web"):
    """Busca y reproduce música de forma inteligente"""

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

def abrir_reproductor_web(servicio, busqueda=None):
    servicios = {
        'youtube': f"https://www.youtube.com/results?search_query={quote(busqueda) if busqueda else ''}",
        'spotify': "https://open.spotify.com/",
        'soundcloud': f"https://soundcloud.com/search?q={quote(busqueda) if busqueda else ''}",
        'apple_music': "https://music.apple.com/",
        'amazon_music': "https://music.amazon.com/",
        'deezer': "https://www.deezer.com/",
        'tidal': "https://tidal.com/"
    }

    if servicio in servicios:
        webbrowser.open(servicios[servicio])
        return f"Abriendo {servicio}"
    else:
        return f"Servicio no disponible. Opciones: {list(servicios.keys())}"
