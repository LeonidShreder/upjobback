from functools import reduce

from database import session
from models.purchase import Purchase
from models.vacancy import Vacancy
from models.employee import Employee
from sqlalchemy import func
from datetime import date

__all__ = [
    "get_quantity",
]


def get_quantity(company_id):
    nb_activated_vacancies = session.query(
        func.count(Vacancy.is_activated).label('act_vacancies')).group_by(
        Vacancy.is_activated).filter(Vacancy.is_activated == "True").first()
    nb_activated_employees = session.query(
        func.count(Employee.is_activated).label('act_employees')).group_by(
        Employee.is_activated).filter(Employee.is_activated == "True").first()
    return session.query((reduce(lambda x, y: x-y if y else x,
                                 [func.sum(Purchase.quantity),
                                  nb_activated_employees,
                                  nb_activated_vacancies])).label(
        'quantity')).group_by(Purchase.company_id).filter(
        (date.today() <= Purchase.expiration_date),
        (Purchase.company_id == company_id)).first()
