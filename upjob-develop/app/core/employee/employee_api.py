from sqlalchemy import update as upd

from database import session
from models.employee import Employee
from models.competence import Competence
from models.technology import Technology
from models.userprofile import UserProfile
from models.company import Company
from models.profession import Profession
from models.experience import Experience
from core.decorators import update

__all__ = [
    "get_employees",
    "get_employee_by_id",
    "get_employee_info_map",
    "update_employee",
]


def get_employees(args):
    employee_list = session.query(Employee, Profession, Competence,
                                  Technology).outerjoin(
        Profession, Profession.id == Employee.profession_id).outerjoin(
        Competence, Competence.employee_id == Employee.id).outerjoin(
        Technology, Competence.technology_id == Technology.id
    )
    if args.get('value'):
        employee_list = employee_list.filter(
            Profession.value.in_(args.get('value')))
    if args.get('technologies'):
        employee_list = employee_list.filter(
            Technology.id.in_(args.get('technologies')))

    return employee_list


def get_employee_info_map(employee_list):
    ALL_FIELDS_TABLE = session.query(
        Employee, Competence, Experience, Technology, UserProfile, Company,
        Profession).outerjoin(
        Competence, Competence.employee_id == Employee.id).outerjoin(
        Experience, Experience.id == Competence.experience_id).outerjoin(
        Technology, Technology.id == Competence.technology_id).outerjoin(
        UserProfile, UserProfile.id == Employee.user_id).outerjoin(
        Company, UserProfile.company_id == Company.id).outerjoin(
        Profession, Profession.id == Employee.profession_id).all()
    dict_employee_info_map = {}
    for line_table in ALL_FIELDS_TABLE:
        dict_employee_fields = {
            'competence': []
        }
        if dict_employee_info_map.get(str(line_table.Employee.id)) is None:
            dict_employee_fields['company'] = line_table.Company.title
            dict_employee_fields['profession'] = line_table.Profession.name
            if line_table.Technology:
                dict_employee_fields['competence'].append(
                    {'id': line_table.Technology.id,
                     'name': line_table.Technology.name,
                     'experience': line_table.Experience.experience_value})
            dict_employee_info_map[
                str(line_table.Employee.id)] = dict_employee_fields
        else:
            dict_employee_info_map.get(str(1)).get('competence').append(
                {'id': line_table.Technology.id,
                 'name': line_table.Technology.name,
                 'experience': line_table.Experience.experience_value})
    return dict_employee_info_map


def get_employee_by_id(args):
    return session.query(Employee).get(args.get('id'))


@update
def update_employee(args):
    args['id'] = int(args.get('id'))
    args['is_activated'] = args.get('is_activated') == 'True'
    return upd(Employee).where(Employee.id == args.get('id')).values(**args)
