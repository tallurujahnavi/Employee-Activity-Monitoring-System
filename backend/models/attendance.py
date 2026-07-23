from datetime import datetime
from utils.database import db


class Attendance(db.Model):
    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    login_time = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    logout_time = db.Column(
        db.DateTime,
        nullable=True
    )

    total_hours = db.Column(
        db.Float,
        default=0
    )

    attendance_date = db.Column(
        db.Date,
        default=lambda: datetime.utcnow().date
    )

    employee = db.relationship(
        "Employee",
        backref="attendance_records"
    )

    def __repr__(self):
        return f"<Attendance {self.employee_id}>"