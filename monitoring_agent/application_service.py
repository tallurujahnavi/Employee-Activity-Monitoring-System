import time

from application_tracker import ApplicationTracker
from api_client import post
from config import EMPLOYEE_ID


def start_application_monitor():

    print("Application Monitoring Started...")

    previous_app = ""

    while True:

        app = ApplicationTracker.get_active_application()

        current_app = app["application_name"]

        if current_app != previous_app:

            post(
                "application/log",
                {
                    "employee_id": EMPLOYEE_ID,
                    "application_name": app["application_name"],
                    "window_title": app["window_title"]
                }
            )

            previous_app = current_app

        time.sleep(3)