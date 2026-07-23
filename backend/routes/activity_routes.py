from flask import Blueprint, request, jsonify
from services.activity_service import ActivityService

activity_bp = Blueprint(
    "activity",
    __name__,
    url_prefix="/api/activity"
)


@activity_bp.route("/update", methods=["POST"])
def update_activity():

    data = request.get_json()

    employee_id = data["employee_id"]

    result = ActivityService.update_activity(
        employee_id,
        data
    )

    return jsonify(result)


@activity_bp.route("/", methods=["GET"])
def get_activity():

    return jsonify(
        ActivityService.get_all_activity()
    )