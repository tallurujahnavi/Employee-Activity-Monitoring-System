import time

from usb_tracker import USBTracker
from api_client import post
from config import EMPLOYEE_ID


def start_usb_monitor():

    print("🔌 USB Monitoring Started...")

    USBTracker.previous_devices = USBTracker.get_usb_devices()

    while True:

        time.sleep(2)

        current_devices = USBTracker.get_usb_devices()

        connected = current_devices - USBTracker.previous_devices
        disconnected = USBTracker.previous_devices - current_devices

        for device in connected:

            print(f"USB Connected: {device}")

            post(
                "usb/log",
                {
                    "employee_id": EMPLOYEE_ID,
                    "device_name": device,
                    "device_id": device,
                    "vendor_name": "Unknown",
                    "action": "Connected"
                }
            )

        for device in disconnected:

            print(f"USB Disconnected: {device}")

            post(
                "usb/log",
                {
                    "employee_id": EMPLOYEE_ID,
                    "device_name": device,
                    "device_id": device,
                    "vendor_name": "Unknown",
                    "action": "Disconnected"
                }
            )

        USBTracker.previous_devices = current_devices