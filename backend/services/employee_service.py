from models.employee import Employee
from services.auth_service import AuthService
from utils.database import db


class EmployeeService:

    @staticmethod
    def add_employee(data):
        """
        Add a new employee
        """

        existing_employee = Employee.query.filter_by(
            email=data["email"]
        ).first()

        if existing_employee:
            return {
                "success": False,
                "message": "Employee already exists."
            }

        employee = Employee(
            employee_id=data["employee_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data.get("phone"),
            department=data.get("department"),
            designation=data.get("designation"),
            password=AuthService.hash_password(
                data["password"]
            ),
            status="Active"
        )

        db.session.add(employee)
        db.session.commit()

        return {
            "success": True,
            "message": "Employee added successfully."
        }

    @staticmethod
    def get_all_employees():
        """
        Return all employees
        """

        employees = Employee.query.all()

        result = []

        for emp in employees:
            result.append({
                "id": emp.id,
                "employee_id": emp.employee_id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "email": emp.email,
                "phone": emp.phone,
                "department": emp.department,
                "designation": emp.designation,
                "status": emp.status,
                "created_at": emp.created_at
            })

        return result

    @staticmethod
    def get_employee(employee_id):
        """
        Get employee by database ID
        """

        employee = Employee.query.get(employee_id)

        if not employee:
            return None

        return {
            "id": employee.id,
            "employee_id": employee.employee_id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "phone": employee.phone,
            "department": employee.department,
            "designation": employee.designation,
            "status": employee.status,
            "created_at": employee.created_at
        }

    @staticmethod
    def update_employee(employee_id, data):
        """
        Update employee details
        """

        employee = Employee.query.get(employee_id)

        if not employee:
            return {
                "success": False,
                "message": "Employee not found."
            }

        employee.first_name = data.get(
            "first_name",
            employee.first_name
        )

        employee.last_name = data.get(
            "last_name",
            employee.last_name
        )

        employee.email = data.get(
            "email",
            employee.email
        )

        employee.phone = data.get(
            "phone",
            employee.phone
        )

        employee.department = data.get(
            "department",
            employee.department
        )

        employee.designation = data.get(
            "designation",
            employee.designation
        )

        employee.status = data.get(
            "status",
            employee.status
        )

        db.session.commit()

        return {
            "success": True,
            "message": "Employee updated successfully."
        }

    @staticmethod
    def delete_employee(employee_id):
        """
        Delete employee
        """

        employee = Employee.query.get(employee_id)

        if not employee:
            return {
                "success": False,
                "message": "Employee not found."
            }

        db.session.delete(employee)
        db.session.commit()

        return {
            "success": True,
            "message": "Employee deleted successfully."
        }

    @staticmethod
    def search_employee(keyword):
        """
        Search employees by first name, last name,
        employee ID, email or department
        """

        employees = Employee.query.filter(
            (Employee.first_name.ilike(f"%{keyword}%")) |
            (Employee.last_name.ilike(f"%{keyword}%")) |
            (Employee.employee_id.ilike(f"%{keyword}%")) |
            (Employee.email.ilike(f"%{keyword}%")) |
            (Employee.department.ilike(f"%{keyword}%"))
        ).all()

        result = []

        for emp in employees:
            result.append({
                "id": emp.id,
                "employee_id": emp.employee_id,
                "first_name": emp.first_name,
                "last_name": emp.last_name,
                "email": emp.email,
                "phone": emp.phone,
                "department": emp.department,
                "designation": emp.designation,
                "status": emp.status
            })

        return result