from core.company.company_api import (
    create_company,
    delete_company_by_id,
    get_companies,
    get_company_by_id,
    update_company_by_id,
)
from core.company.validators import validate_company_by_email


__all__ = [
    'Company',
    'CompanyInList',
]


class BaseCompany(object):
    """Represent base company item.
    """
    def __init__(self, doc, size):
        self.id = str(doc.id)
        self.title = doc.title
        self.address = doc.address
        self.description = doc.description
        self.size = size
        self.phone_number = doc.phone_number
        self.email = doc.email


class CompanyInList(BaseCompany):
    """Represent company item in list.
    """
    def __init__(self, doc, size):
        super(CompanyInList, self).__init__(doc, size)

    @staticmethod
    def get_all(args):
        company_list = get_companies(args)
        return [CompanyInList(c.Company, c.CompanyRange.size_name) for c in company_list]


class Company(BaseCompany):
    """Represent single company item.
    """
    def __init__(self, doc, size):
        super(Company, self).__init__(doc, size)

    @staticmethod
    def get_company(company_id):
        doc = get_company_by_id(company_id)
        return doc and Company(doc.Company, doc.CompanyRange.size_value)

    @staticmethod
    def create_company(args):
        doc = create_company(args)
        return doc and Company(doc, doc.size_range_id)

    @staticmethod
    def delete_company(company_id):
        doc = delete_company_by_id(company_id)
        return doc and Company(doc.Company, doc.Company.size_range_id)

    @staticmethod
    def validate_company_by_email(email):
        return validate_company_by_email(email)

    @staticmethod
    def update_company(company_id, args):
        update_company_by_id(company_id, args)
        doc = get_company_by_id(company_id)
        return doc and Company(doc.Company, doc.CompanyRange.size_value)

