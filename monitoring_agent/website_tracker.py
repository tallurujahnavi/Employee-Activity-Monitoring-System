import win32gui
import win32process
import psutil


class WebsiteTracker:

    BROWSERS = [
        "chrome.exe",
        "msedge.exe",
        "firefox.exe",
        "brave.exe"
    ]

    @staticmethod
    def get_browser_activity():

        try:
            hwnd = win32gui.GetForegroundWindow()

            title = win32gui.GetWindowText(hwnd)

            _, pid = win32process.GetWindowThreadProcessId(hwnd)

            process = psutil.Process(pid)

            process_name = process.name()

            print("Process:", process_name)
            print("Window Title:", title)

            if process_name.lower() in WebsiteTracker.BROWSERS:
                return {
                    "browser_name": process_name,
                    "website_title": title
                }

            return None

        except Exception as e:
            print("Error:", e)
            return None