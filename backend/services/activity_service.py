from datetime import datetime
from models.activity import Activity
from utils.database import db


class ActivityService:

    @staticmethod
    def update_activity(employee_id, data):

        activity = Activity.query.filter_by(
            employee_id=employee_id
        ).first()

        if not activity:
            activity = Activity(
                employee_id=employee_id
            )
            db.session.add(activity)

        activity.login_status = data.get(
            "login_status",
            activity.login_status
        )

        activity.current_status = data.get(
            "current_status",
            activity.current_status
        )

        activity.active_time = data.get(
            "active_time",
            activity.active_time
        )

        activity.idle_time = data.get(
            "idle_time",
            activity.idle_time
        )

        activity.last_activity = datetime.utcnow()

        db.session.commit()

        return {
            "success": True,
            "message": "Activity updated successfully."
        }

    @staticmethod
    def get_all_activity():

        activities = Activity.query.all()

        result = []

        for activity in activities:

            result.append({
                "employee_id": activity.employee_id,
                "login_status": activity.login_status,
                "current_status": activity.current_status,
                "active_time": activity.active_time,
                "idle_time": activity.idle_time,
                "last_activity": activity.last_activity
            })

        return result