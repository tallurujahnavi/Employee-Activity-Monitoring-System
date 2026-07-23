from datetime import datetime
from utils.database import db


class USBLog(db.Model):
    __tablename__ = "usb_logs"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    device_name = db.Column(
        db.String(255),
        nullable=False
    )

    device_id = db.Column(
        db.String(255),
        nullable=False
    )

    vendor_name = db.Column(
        db.String(255),
        nullable=True
    )

    action = db.Column(
        db.String(20),
        nullable=False
    )

    action_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="usb_logs"
    )

    def __repr__(self):
        return f"<USBLog {self.device_name}>"