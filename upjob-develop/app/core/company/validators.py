from core.company.company_api import get_companies


__all__ = [
    "validate_company_by_email",
]


def validate_company_by_email(email):
    return get_companies({'email': email}).count() > 0
