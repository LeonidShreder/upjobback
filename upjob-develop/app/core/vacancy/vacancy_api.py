from sqlalchemy import update as upd

from database import session
from models.vacancy import Vacancy
from models.requirement import Requirement
from models.technology import Technology
from models.userprofile import UserProfile
from models.company import Company
from models.profession import Profession
from models.experience import Experience
from core.decorators import update


def get_vacancies(args):
    vacancy_list = session.query(Vacancy, Profession, Requirement,
                                 Technology).outerjoin(
        Profession, Profession.id == Vacancy.profession_id).outerjoin(
        Requirement, Requirement.vacancy_id == Vacancy.id).outerjoin(
        Technology, Requirement.technology_id == Technology.id
    )
    if args.get('value'):
        vacancy_list = vacancy_list.filter(
            Profession.value.in_(args.get('value')))
    if args.get('technologies'):
        vacancy_list = vacancy_list.filter(
            Technology.id.in_(args.get('technologies')))
    if args.get('is_activated'):
        vacancy_list = vacancy_list.filter(
            Vacancy.is_activated == args.get('technologies')
        )
    return vacancy_list


def get_vacancy_info_map(vacancy_list):
    ALL_FIELDS_TABLE = session.query(
        Vacancy, Requirement, Experience, Technology, UserProfile, Company,
        Profession).outerjoin(
        Requirement, Requirement.vacancy_id == Vacancy.id).outerjoin(
        Experience, Experience.id == Requirement.experience_id).outerjoin(
        Technology, Technology.id == Requirement.technology_id).outerjoin(
        UserProfile, UserProfile.id == Vacancy.user_id).outerjoin(
        Company, UserProfile.company_id == Company.id).outerjoin(
        Profession, Vacancy.profession_id == Profession.id
    ).all()
    dict_vacancy_info_map = {}
    for line_table in ALL_FIELDS_TABLE:
        dict_vacancy_fields = {
            'requirement': []
        }
        if dict_vacancy_info_map.get(str(line_table.Vacancy.id)) is None:
            dict_vacancy_fields['company'] = line_table.Company.title
            dict_vacancy_fields['profession'] = line_table.Profession.name
            if line_table.Technology:
                dict_vacancy_fields['requirement'].append(
                    {'id': line_table.Technology.id,
                     'name': line_table.Technology.name,
                     'experience': line_table.Experience.experience_value})
            dict_vacancy_info_map[
                str(line_table.Vacancy.id)] = dict_vacancy_fields
        else:
            dict_vacancy_info_map.get(str(1)).get('requirement').append(
                {'id': line_table.Technology.id,
                 'name': line_table.Technology.name,
                 'experience': line_table.Experience.experience_value})
    return dict_vacancy_info_map


def get_vacancy_by_id(args):
    return session.query(Vacancy).get(args.get('id'))


@update
def update_vacancy_by_id(args):
    args['id'] = int(args.get('id'))
    args['is_activated'] = args.get('is_activated') == 'True'
    return upd(Vacancy).where(Vacancy.id == int(args.get('id'))).values(**args)
