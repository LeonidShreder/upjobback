from core.employee.employee_api import (
    get_employees,
    get_employee_by_id,
    get_employee_info_map,
    update_employee,
)

__all__ = [
    'Employee',
    'EmployeeInList',
]


class BaseEmployee:
    """
    Represent base employee item.
    """

    def __init__(self, doc, employee_company_map):
        try:
            doc = doc.Employee
        except AttributeError:
            doc = doc
        self.id = str(doc.id)
        self.title = doc.title
        self.full_name = doc.full_name
        self.user_id = doc.user_id
        self.is_activated = doc.is_activated
        self.public_id = doc.public_id
        self.portfolio = doc.portfolio
        employee_fields = employee_company_map.get(self.id)
        if employee_fields is not None:
            self.company = employee_fields.get('company')
            self.profession = employee_fields.get('profession')
            self.competences = []
            for competence in employee_fields.get('competence'):
                self.competences.append({'id': competence.get('id'),
                                        'name': competence.get('name'),
                                        'experience':
                                             competence.get('experience'),
                                        })


class EmployeeInList(BaseEmployee):
    """
    Represent employee item in list.
    """

    def __init__(self, doc, employee_company_map):
        super().__init__(doc, employee_company_map)

    @staticmethod
    def get_all(args):
        employee_list = get_employees(args)
        employee_info_map = get_employee_info_map(employee_list)
        return [EmployeeInList(e, employee_info_map) for e in employee_list]


class Employee(BaseEmployee):
    """
    Represent an employee item.
    """

    def __init__(self, doc, employee_company_map):
        super().__init__(doc, employee_company_map)

    @staticmethod
    def get_employee(args):
        doc = get_employee_by_id(args)
        employee_info_map = get_employee_info_map(doc)
        return Employee(doc, employee_info_map)

    @staticmethod
    def put_employee(args):
        update_employee(args)
        doc = get_employee_by_id(args)
        employee_info_map = get_employee_info_map(doc)
        return Employee(doc, employee_info_map)
