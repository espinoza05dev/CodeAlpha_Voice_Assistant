import webbrowser
import subprocess
import os
import platform
from urllib.parse import quote_plus

class BrowserSearchController:
    def __init__(self):
        self.available_browsers = self.detect_browsers()

    def detect_browsers(self):
        browsers = {}
        system = platform.system().lower()

        if system == "windows":
            browser_paths = {
                'chrome': [
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                ],
                'firefox': [
                    r"C:\Program Files\Mozilla Firefox\firefox.exe",
                    r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
                ],
                'edge': [
                    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                    r"C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\MicrosoftEdge.exe"
                ],
                'opera': [
                    r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera\opera.exe",
                    r"C:\Program Files\Opera\opera.exe"
                ],
                'brave': [
                    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
                    r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
                ]
            }
        elif system == "darwin":  # macOS
            browser_paths = {
                'chrome': ["/Applications/Google Chrome.app"],
                'firefox': ["/Applications/Firefox.app"],
                'safari': ["/Applications/Safari.app"],
                'opera': ["/Applications/Opera.app"],
                'brave': ["/Applications/Brave Browser.app"]
            }
        else:  # Linux
            browser_paths = {
                'chrome': ["google-chrome", "google-chrome-stable"],
                'firefox': ["firefox"],
                'opera': ["opera"],
                'brave': ["brave-browser"]
            }

        for browser, paths in browser_paths.items():
            for path in paths:
                if system == "linux":
                    try:
                        subprocess.run([path, "--version"], capture_output=True, timeout=5)
                        browsers[browser] = path
                        break
                    except:
                        continue
                else:
                    expanded_path = os.path.expandvars(path)
                    if os.path.exists(expanded_path):
                        browsers[browser] = expanded_path
                        break

        return browsers

    def search_with_browser(self, browser_name=None, search_query="", search_engine="google"):

        search_engines = {
            'google': f"https://www.google.com/search?q={quote_plus(search_query)}",
            'bing': f"https://www.bing.com/search?q={quote_plus(search_query)}",
            'duckduckgo': f"https://duckduckgo.com/?q={quote_plus(search_query)}",
            'yahoo': f"https://search.yahoo.com/search?p={quote_plus(search_query)}",
            'yandex': f"https://yandex.com/search/?text={quote_plus(search_query)}"
        }

        search_url = search_engines.get(search_engine.lower(), search_engines['google'])

        try:
            if browser_name and browser_name.lower() in self.available_browsers:
                browser_path = self.available_browsers[browser_name.lower()]

                if platform.system().lower() == "windows":
                    subprocess.Popen([browser_path, search_url])
                elif platform.system().lower() == "darwin":  # macOS
                    subprocess.Popen(["open", "-a", browser_path, search_url])
                else:  # Linux
                    subprocess.Popen([browser_path, search_url])

                return f"Opened {browser_name} and searched for '{search_query}' on {search_engine}"
            else:
                webbrowser.open(search_url)
                return f"Searched for '{search_query}' on {search_engine} using default browser"

        except Exception as e:
            try:
                webbrowser.open(search_url)
                return f"Opened default browser and searched for '{search_query}'"
            except Exception as e2:
                return f"Error opening browser: {e2}"

    def open_browser(self, browser_name=None, url="https://www.google.com"):
        try:
            if browser_name and browser_name.lower() in self.available_browsers:
                browser_path = self.available_browsers[browser_name.lower()]

                if platform.system().lower() == "windows":
                    subprocess.Popen([browser_path, url])
                elif platform.system().lower() == "darwin":  # macOS
                    subprocess.Popen(["open", "-a", browser_path, url])
                else:  # Linux
                    subprocess.Popen([browser_path, url])

                return f"Opened {browser_name}"
            else:
                webbrowser.open(url)
                return f"Opened default browser"
        except Exception as e:
            return f"Error opening browser: {e}"

    def get_available_browsers(self):
        return list(self.available_browsers.keys())

    def search_youtube(self, query):
        url = f"https://www.youtube.com/results?search_query={quote_plus(query)}"
        webbrowser.open(url)
        return f"Searching YouTube for '{query}'"

    def search_wikipedia(self, query, language="en"):
        url = f"https://{language}.wikipedia.org/wiki/Special:Search?search={quote_plus(query)}"
        webbrowser.open(url)
        return f"Searching Wikipedia for '{query}'"

    def open_social_media(self, platform):
        social_urls = {
            'facebook': 'https://www.facebook.com',
            'twitter': 'https://www.twitter.com',
            'instagram': 'https://www.instagram.com',
            'linkedin': 'https://www.linkedin.com',
            'tiktok': 'https://www.tiktok.com',
            'reddit': 'https://www.reddit.com'
        }

        platform_lower = platform.lower()
        if platform_lower in social_urls:
            webbrowser.open(social_urls[platform_lower])
            return f"Opened {platform}"
        else:
            return f"Unknown social media platform: {platform}"

browser_controller = BrowserSearchController()


def search_web(query, browser=None, search_engine="google"):
    return browser_controller.search_with_browser(browser, query, search_engine)


def open_browser_simple(browser=None):
    return browser_controller.open_browser(browser)


def get_browsers():
    return browser_controller.get_available_browsers()