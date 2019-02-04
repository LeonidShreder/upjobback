from flask_restful import fields

__all__ = [
    'company_list_schema',
    'company_schema',
]

base_company_schema = dict(
    id=fields.String,
    title=fields.String,
    address=fields.String,
    description=fields.String,
    phone_number=fields.String,
    email=fields.String,
    size=fields.String,
)

company_list_schema = dict(
    base_company_schema,
)

company_schema = dict(
    base_company_schema,
)
