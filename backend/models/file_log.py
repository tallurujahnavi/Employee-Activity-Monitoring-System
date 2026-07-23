from datetime import datetime
from utils.database import db


class FileLog(db.Model):
    __tablename__ = "file_logs"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    file_path = db.Column(
        db.String(500),
        nullable=False
    )

    action = db.Column(
        db.String(50),
        nullable=False
    )

    action_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    employee = db.relationship(
        "Employee",
        backref="file_logs"
    )

    def __repr__(self):
        return f"<FileLog {self.file_name}>"