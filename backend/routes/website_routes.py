from flask import Blueprint, request, jsonify
from services.website_service import WebsiteService

website_bp = Blueprint(
    "website",
    __name__,
    url_prefix="/api/website"
)


@website_bp.route("/log", methods=["POST"])
def save():

    data = request.get_json()

    return jsonify(
        WebsiteService.save_website(data)
    )


@website_bp.route("/", methods=["GET"])
def get():

    return jsonify(
        WebsiteService.get_all()
    )