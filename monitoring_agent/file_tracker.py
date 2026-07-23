from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class FileTracker(FileSystemEventHandler):

    def on_created(self, event):
        if not event.is_directory:
            print(f"Created: {event.src_path}")

    def on_modified(self, event):
        if not event.is_directory:
            print(f"Modified: {event.src_path}")

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"Deleted: {event.src_path}")


def start_tracking(path):

    event_handler = FileTracker()

    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)

    observer.start()

    print("File Monitoring Started...")
    print("Watching:", path)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()