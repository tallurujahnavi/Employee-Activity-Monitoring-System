import psutil
import time


class USBTracker:

    previous_devices = set()

    @staticmethod
    def get_usb_devices():

        devices = set()

        for partition in psutil.disk_partitions():

            if "removable" in partition.opts.lower():
                devices.add(partition.device)

        return devices


def start_usb_monitor():

    print("USB Monitoring Started...")

    USBTracker.previous_devices = USBTracker.get_usb_devices()

    while True:

        time.sleep(2)

        current_devices = USBTracker.get_usb_devices()

        connected = current_devices - USBTracker.previous_devices
        disconnected = USBTracker.previous_devices - current_devices

        for device in connected:
            print(f"USB Connected: {device}")

        for device in disconnected:
            print(f"USB Disconnected: {device}")

        USBTracker.previous_devices = current_devices