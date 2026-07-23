from datetime import datetime
from models.file_log import FileLog
from utils.database import db


class FileService:

    @staticmethod
    def save_file(data):

        log = FileLog(
            employee_id=data["employee_id"],
            file_name=data["file_name"],
            file_path=data["file_path"],
            action=data["action"],
            action_time=datetime.utcnow()
        )

        db.session.add(log)
        db.session.commit()

        return {
            "success": True,
            "message": "File activity saved successfully."
        }

    @staticmethod
    def get_all():

        logs = FileLog.query.order_by(
            FileLog.action_time.desc()
        ).all()

        result = []

        for log in logs:

            result.append({
                "id": log.id,
                "employee_id": log.employee_id,
                "file_name": log.file_name,
                "file_path": log.file_path,
                "action": log.action,
                "action_time": log.action_time
            })

        return result