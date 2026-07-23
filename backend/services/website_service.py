from datetime import datetime
from models.website_log import WebsiteLog
from utils.database import db


class WebsiteService:

    @staticmethod
    def save_website(data):

        log = WebsiteLog(
            employee_id=data["employee_id"],
            website_title=data["website_title"],
            website_url=data.get("website_url", data["website_title"]),
            browser_name=data["browser_name"],
            start_time=datetime.utcnow()
        )

        db.session.add(log)
        db.session.commit()

        return {
            "success": True,
            "message": "Website activity saved successfully."
        }

    @staticmethod
    def get_all():

        logs = WebsiteLog.query.order_by(
            WebsiteLog.start_time.desc()
        ).all()

        result = []

        for log in logs:
            result.append({
                "id": log.id,
                "employee_id": log.employee_id,
                "website_title": log.website_title,
                "website_url": log.website_url,
                "browser_name": log.browser_name,
                "start_time": log.start_time,
                "end_time": log.end_time,
                "duration_minutes": log.duration_minutes
            })

        return result