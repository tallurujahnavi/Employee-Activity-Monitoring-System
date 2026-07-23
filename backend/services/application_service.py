from datetime import datetime
from models.application_log import ApplicationLog
from utils.database import db


class ApplicationService:

    @staticmethod
    def save_application(data):

        log = ApplicationLog(
            employee_id=data["employee_id"],
            application_name=data["application_name"],
            process_name=data["application_name"],
            start_time=datetime.utcnow()
        )

        db.session.add(log)
        db.session.commit()

        return {
            "success": True,
            "message": "Application log saved successfully."
        }

    @staticmethod
    def get_application_logs():

        logs = ApplicationLog.query.order_by(
            ApplicationLog.start_time.desc()
        ).all()

        result = []

        for log in logs:

            result.append({
                "id": log.id,
                "employee_id": log.employee_id,
                "application_name": log.application_name,
                "process_name": log.process_name,
                "start_time": log.start_time,
                "end_time": log.end_time,
                "duration_minutes": log.duration_minutes
            })

        return result