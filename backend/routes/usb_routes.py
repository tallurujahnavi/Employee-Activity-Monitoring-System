from flask import Blueprint, request, jsonify
from services.usb_service import USBService

usb_bp = Blueprint(
    "usb",
    __name__,
    url_prefix="/api/usb"
)


@usb_bp.route("/log", methods=["POST"])
def save():

    data = request.get_json()

    return jsonify(
        USBService.save_usb(data)
    )


@usb_bp.route("/", methods=["GET"])
def get():

    return jsonify(
        USBService.get_all()
    )