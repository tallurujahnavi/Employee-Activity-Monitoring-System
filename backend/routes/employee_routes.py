from flask import Blueprint, request, jsonify

from services.employee_service import EmployeeService

employee_bp = Blueprint(
    "employee",
    __name__,
    url_prefix="/api/employees"
)


# -------------------------
# Add Employee
# -------------------------
@employee_bp.route("/", methods=["POST"])
def add_employee():

    data = request.get_json()

    result = EmployeeService.add_employee(data)

    status = 201 if result["success"] else 400

    return jsonify(result), status


# -------------------------
# Get All Employees
# -------------------------
@employee_bp.route("/", methods=["GET"])
def get_all_employees():

    employees = EmployeeService.get_all_employees()

    return jsonify(employees), 200


# -------------------------
# Get Employee By ID
# -------------------------
@employee_bp.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):

    employee = EmployeeService.get_employee(employee_id)

    if not employee:
        return jsonify({
            "success": False,
            "message": "Employee not found."
        }), 404

    return jsonify(employee), 200


# -------------------------
# Update Employee
# -------------------------
@employee_bp.route("/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    data = request.get_json()

    result = EmployeeService.update_employee(
        employee_id,
        data
    )

    status = 200 if result["success"] else 404

    return jsonify(result), status


# -------------------------
# Delete Employee
# -------------------------
@employee_bp.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    result = EmployeeService.delete_employee(
        employee_id
    )

    status = 200 if result["success"] else 404

    return jsonify(result), status


# -------------------------
# Search Employee
# -------------------------
@employee_bp.route("/search/<string:keyword>", methods=["GET"])
def search_employee(keyword):

    employees = EmployeeService.search_employee(keyword)

    return jsonify(employees), 200