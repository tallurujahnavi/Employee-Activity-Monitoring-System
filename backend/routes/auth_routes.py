from flask import Blueprint, request, jsonify

from models.admin import Admin
from services.auth_service import AuthService
from utils.database import db

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# ----------------------------
# Admin Registration
# ----------------------------
@auth_bp.route("/admin/register", methods=["POST"])
def admin_register():
    """
    Register a new admin
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required."
        }), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "success": False,
            "message": "Username, email and password are required."
        }), 400

    # Check if admin already exists
    existing_admin = Admin.query.filter_by(email=email).first()

    if existing_admin:
        return jsonify({
            "success": False,
            "message": "Admin already exists."
        }), 409

    # Create admin
    new_admin = Admin(
        username=username,
        email=email,
        password=AuthService.hash_password(password)
    )

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({
        "success": True,
        "message": "Admin registered successfully."
    }), 201


# ----------------------------
# Admin Login
# ----------------------------
@auth_bp.route("/admin/login", methods=["POST"])
def admin_login():
    """
    Admin Login API
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "Request body is required."
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required."
        }), 400

    result = AuthService.admin_login(email, password)

    if result["success"]:
        return jsonify(result), 200

    return jsonify(result), 401


# ----------------------------
# Get Admin Profile
# ----------------------------
@auth_bp.route("/admin/profile", methods=["GET"])
def admin_profile():
    """
    Placeholder profile endpoint.
    JWT protection will be added in the next step.
    """

    return jsonify({
        "success": True,
        "message": "Profile endpoint is ready."
    }), 200