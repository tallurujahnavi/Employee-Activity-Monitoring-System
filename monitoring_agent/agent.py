import threading
import time

from activity_tracker import ActivityTracker
from api_client import post
from config import EMPLOYEE_ID

from application_service import start_application_monitor
from website_service import start_website_monitor
from file_service import start_file_monitor
from usb_service import start_usb_monitor


tracker = ActivityTracker()


def activity_monitor():

    tracker.start()

    while True:

        post(
            "activity/update",
            {
                "employee_id": EMPLOYEE_ID,
                "login_status": "Online",
                "current_status": tracker.status,
                "active_time": tracker.active_time,
                "idle_time": tracker.idle_time
            }
        )

        time.sleep(10)


if __name__ == "__main__":

    print("=" * 50)
    print("Employee Activity Monitoring Agent Started")
    print("=" * 50)

    # Activity Monitoring
    threading.Thread(
        target=activity_monitor,
        daemon=True
    ).start()

    # Application Monitoring
    threading.Thread(
        target=start_application_monitor,
        daemon=True
    ).start()

    # Website Monitoring
    threading.Thread(
        target=start_website_monitor,
        daemon=True
    ).start()

    # File Monitoring
    threading.Thread(
        target=start_file_monitor,
        daemon=True
    ).start()

    # USB Monitoring
    threading.Thread(
        target=start_usb_monitor,
        daemon=True
    ).start()

    # Keep main thread alive
    while True:
        time.sleep(1)