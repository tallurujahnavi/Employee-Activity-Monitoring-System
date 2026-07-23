from datetime import datetime
from utils.database import db


class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    login_status = db.Column(
        db.String(20),
        default="Offline"
    )

    current_status = db.Column(
        db.String(20),
        default="Offline"
    )

    active_time = db.Column(
        db.Float,
        default=0
    )

    idle_time = db.Column(
        db.Float,
        default=0
    )

    last_activity = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="activity_records"
    )

    def __repr__(self):
        return f"<Activity Employee ID: {self.employee_id}>"