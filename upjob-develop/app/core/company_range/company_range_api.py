from database import session
from models.company_range import CompanyRange

__all__ = [
    "get_ranges",
]


def get_ranges():
    return session.query(CompanyRange).all()
