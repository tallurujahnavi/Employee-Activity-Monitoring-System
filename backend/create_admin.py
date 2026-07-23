from app import app
from models.admin import Admin
from services.auth_service import AuthService
from utils.database import db

with app.app_context():

    email = "admin@example.com"

    existing_admin = Admin.query.filter_by(email=email).first()

    if existing_admin:
        print("✅ Admin already exists.")
    else:
        admin = Admin(
            username="admin",
            email=email,
            password=AuthService.hash_password("admin123")
        )

        db.session.add(admin)
        db.session.commit()

        print("✅ Admin created successfully!")
        print("Email: admin@example.com")
        print("Password: admin123")