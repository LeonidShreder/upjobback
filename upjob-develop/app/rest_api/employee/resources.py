from flask_restful import Resource, abort, marshal_with

from .items import Employee, EmployeeInList
from .parsers import get_employee_parser, put_employee_parser
from .schemas import employee_list_schema, employee_schema


class EmployeeListResource(Resource):
    """
    Represent employee list.
    """

    @marshal_with(employee_list_schema)
    def get(self):
        args = get_employee_parser.parse_args()
        employees = EmployeeInList.get_all(args)
        return employees, 200


class EmployeeResource(Resource):
    """
    Represent an employee.
    """

    @marshal_with(employee_schema)
    def get(self, employee_id):
        employee = Employee.get_employee(employee_id)
        if employee:
            return employee, 200
        else:
            abort(404, message="Employee not found")

    @marshal_with(employee_schema)
    def put(self):
        args = put_employee_parser.parse_args()
        employee = Employee.put_employee(args)
        if employee:
            return employee, 200
        else:
            abort(404, message="Employee not found")
