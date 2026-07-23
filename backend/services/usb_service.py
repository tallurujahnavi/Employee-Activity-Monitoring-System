from datetime import datetime
from models.usb_log import USBLog
from utils.database import db


class USBService:

    @staticmethod
    def save_usb(data):

        log = USBLog(
            employee_id=data["employee_id"],
            device_name=data["device_name"],
            device_id=data["device_id"],
            vendor_name=data.get("vendor_name"),
            action=data["action"],
            action_time=datetime.utcnow()
        )

        db.session.add(log)
        db.session.commit()

        return {
            "success": True,
            "message": "USB activity saved successfully."
        }

    @staticmethod
    def get_all():

        logs = USBLog.query.order_by(
            USBLog.action_time.desc()
        ).all()

        return [
            {
                "id": log.id,
                "employee_id": log.employee_id,
                "device_name": log.device_name,
                "device_id": log.device_id,
                "vendor_name": log.vendor_name,
                "action": log.action,
                "action_time": log.action_time
            }
            for log in logs
        ]