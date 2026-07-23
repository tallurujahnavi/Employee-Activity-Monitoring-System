import threading
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from api_client import post
from config import EMPLOYEE_ID


class FileHandler(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            self.send_log(event.src_path, "Created")

    def on_modified(self, event):
        if not event.is_directory:
            self.send_log(event.src_path, "Modified")

    def on_deleted(self, event):
        if not event.is_directory:
            self.send_log(event.src_path, "Deleted")

    def send_log(self, path, action):

        filename = path.split("\\")[-1]

        post(
            "file/log",
            {
                "employee_id": EMPLOYEE_ID,
                "file_name": filename,
                "file_path": path,
                "action": action
            }
        )

        print(f"{action}: {filename}")


def start_file_monitor():

    path = "C:\\Users\\Public\\Documents"

    event_handler = FileHandler()

    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)

    observer.start()

    print("📁 File Monitoring Started...")

    try:
        while True:
            threading.Event().wait(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()