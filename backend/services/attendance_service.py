from datetime import datetime
from models.attendance import Attendance
from utils.database import db


class AttendanceService:

    @staticmethod
    def employee_login(employee_id):

        attendance = Attendance(
            employee_id=employee_id,
            login_time=datetime.utcnow(),
            attendance_date=datetime.utcnow().date()
        )

        db.session.add(attendance)
        db.session.commit()

        return {
            "success": True,
            "message": "Login recorded successfully."
        }

    @staticmethod
    def employee_logout(employee_id):

        attendance = Attendance.query.filter_by(
            employee_id=employee_id,
            logout_time=None
        ).order_by(
            Attendance.login_time.desc()
        ).first()

        if not attendance:
            return {
                "success": False,
                "message": "No active login found."
            }

        attendance.logout_time = datetime.utcnow()

        duration = attendance.logout_time - attendance.login_time
        attendance.total_hours = round(
            duration.total_seconds() / 3600,
            2
        )

        db.session.commit()

        return {
            "success": True,
            "message": "Logout recorded successfully."
        }

    @staticmethod
    def get_attendance():

        records = Attendance.query.all()

        result = []

        for record in records:
            result.append({
                "id": record.id,
                "employee_id": record.employee_id,
                "login_time": record.login_time,
                "logout_time": record.logout_time,
                "total_hours": record.total_hours,
                "attendance_date": record.attendance_date
            })

        return result