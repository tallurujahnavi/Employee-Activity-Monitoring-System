import bcrypt
from models.admin import Admin
from utils.jwt_helper import generate_token


class AuthService:
    @staticmethod
    def hash_password(password):
        """
        Hash a plain text password.
        """
        hashed = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password, hashed_password):
        """
        Verify a password against its hash.
        """
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    @staticmethod
    def admin_login(email, password):
        """
        Authenticate an admin user.
        """
        admin = Admin.query.filter_by(email=email).first()

        if not admin:
            return {
                "success": False,
                "message": "Invalid email or password"
            }

        if not AuthService.verify_password(password, admin.password):
            return {
                "success": False,
                "message": "Invalid email or password"
            }

        token = generate_token(str(admin.id))

        return {
            "success": True,
            "message": "Login successful",
            "token": token,
            "admin": {
                "id": admin.id,
                "username": admin.username,
                "email": admin.email
            }
        }