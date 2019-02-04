from sqlalchemy import update as upd

from core.decorators import create, delete, update
from database import session
from models.company import Company
from models.company_range import CompanyRange

__all__ = [
    "create_company",
    "delete_company_by_id",
    "get_companies",
    "get_company_by_id",
    "update_company_by_id",
]


@create
def create_company(company_info):
    return Company(**company_info)


def get_companies(company_info):
    return session.query(Company, CompanyRange).filter_by(**company_info).join(
        CompanyRange, CompanyRange.id == Company.size_range_id).all()


def get_company_by_id(company_id):
    return session.query(Company, CompanyRange).join(
        CompanyRange, CompanyRange.id == Company.size_range_id).filter(
        Company.id == company_id).first()


@delete
def delete_company_by_id(company_id):
    return get_company_by_id(company_id)


@update
def update_company_by_id(company_id, company_info):
    return upd(Company).where(Company.id == company_id).values(**company_info)
