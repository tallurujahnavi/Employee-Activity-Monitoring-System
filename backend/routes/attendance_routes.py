from flask import Blueprint, request, jsonify
from services.attendance_service import AttendanceService

attendance_bp = Blueprint(
    "attendance",
    __name__,
    url_prefix="/api/attendance"
)


@attendance_bp.route("/login", methods=["POST"])
def employee_login():

    data = request.get_json()

    result = AttendanceService.employee_login(
        data["employee_id"]
    )

    return jsonify(result)


@attendance_bp.route("/logout", methods=["POST"])
def employee_logout():

    data = request.get_json()

    result = AttendanceService.employee_logout(
        data["employee_id"]
    )

    return jsonify(result)


@attendance_bp.route("/", methods=["GET"])
def get_attendance():

    return jsonify(
        AttendanceService.get_attendance()
    )