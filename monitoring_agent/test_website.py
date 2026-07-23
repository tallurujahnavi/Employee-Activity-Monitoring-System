import time
from website_tracker import WebsiteTracker

print("You have 5 seconds to click on Chrome/Edge...")
time.sleep(5)

print(WebsiteTracker.get_browser_activity())