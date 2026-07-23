from datetime import datetime
from utils.database import db


class ApplicationLog(db.Model):
    __tablename__ = "application_logs"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    application_name = db.Column(
        db.String(255),
        nullable=False
    )

    process_name = db.Column(
        db.String(255),
        nullable=False
    )

    start_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    end_time = db.Column(
        db.DateTime,
        nullable=True
    )

    duration_minutes = db.Column(
        db.Float,
        default=0
    )

    employee = db.relationship(
        "Employee",
        backref="application_logs"
    )

    def __repr__(self):
        return f"<ApplicationLog {self.application_name}>"