from flask import Blueprint, request, jsonify
from services.application_service import ApplicationService

application_bp = Blueprint(
    "application",
    __name__,
    url_prefix="/api/application"
)


@application_bp.route("/log", methods=["POST"])
def save_application():

    data = request.get_json()

    result = ApplicationService.save_application(data)

    return jsonify(result)


@application_bp.route("/", methods=["GET"])
def get_logs():

    return jsonify(
        ApplicationService.get_application_logs()
    )