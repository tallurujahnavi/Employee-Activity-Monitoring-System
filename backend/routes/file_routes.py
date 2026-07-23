from flask import Blueprint, request, jsonify
from services.file_service import FileService

file_bp = Blueprint(
    "file",
    __name__,
    url_prefix="/api/file"
)


@file_bp.route("/log", methods=["POST"])
def save():

    data = request.get_json()

    return jsonify(
        FileService.save_file(data)
    )


@file_bp.route("/", methods=["GET"])
def get():

    return jsonify(
        FileService.get_all()
    )