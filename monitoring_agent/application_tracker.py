import win32gui
import win32process
import psutil


class ApplicationTracker:

    @staticmethod
    def get_active_application():
        try:
            hwnd = win32gui.GetForegroundWindow()

            _, pid = win32process.GetWindowThreadProcessId(hwnd)

            process = psutil.Process(pid)

            return {
                "application_name": process.name(),
                "window_title": win32gui.GetWindowText(hwnd)
            }

        except Exception:
            return {
                "application_name": "Unknown",
                "window_title": "Unknown"
            }