import threading
import time
from datetime import datetime
from pynput import keyboard, mouse


class ActivityTracker:

    def __init__(self):

        self.last_activity = datetime.now()

        self.active_time = 0

        self.idle_time = 0

        self.status = "Active"

    def on_activity(self, *args):

        self.last_activity = datetime.now()

    def start_listener(self):

        keyboard.Listener(
            on_press=self.on_activity
        ).start()

        mouse.Listener(
            on_move=self.on_activity,
            on_click=self.on_activity,
            on_scroll=self.on_activity
        ).start()

    def monitor(self):

        while True:

            idle_seconds = (
                datetime.now() -
                self.last_activity
            ).total_seconds()

            if idle_seconds < 60:

                self.status = "Active"

                self.active_time += 10

            else:

                self.status = "Idle"

                self.idle_time += 10

            time.sleep(10)

    def start(self):

        self.start_listener()

        threading.Thread(
            target=self.monitor,
            daemon=True
        ).start()