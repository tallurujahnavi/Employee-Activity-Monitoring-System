import time

from website_tracker import WebsiteTracker
from api_client import post
from config import EMPLOYEE_ID


def start_website_monitor():

    print("Website Monitoring Started...")

    previous_title = ""

    while True:

        website = WebsiteTracker.get_browser_activity()

        if website:

            if website["website_title"] != previous_title:

                post(
                    "website/log",
                    {
                        "employee_id": EMPLOYEE_ID,
                        "browser_name": website["browser_name"],
                        "website_title": website["website_title"],
                        "website_url": website["website_title"]
                    }
                )

                previous_title = website["website_title"]

        time.sleep(3)