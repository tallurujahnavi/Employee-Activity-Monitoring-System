from datetime import datetime
from utils.database import db


class WebsiteLog(db.Model):
    __tablename__ = "website_logs"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    website_title = db.Column(
        db.String(255),
        nullable=True
    )

    website_url = db.Column(
        db.String(500),
        nullable=False
    )

    browser_name = db.Column(
        db.String(100),
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
        backref="website_logs"
    )

    def __repr__(self):
        return f"<WebsiteLog {self.website_url}>"