from flask_restful import fields

__all__ = [
    'company_range_schema',
]

base_company_range_schema = dict(
    id=fields.String,
    size_name=fields.String,
    size_value=fields.String,
)

company_range_schema = dict(
    base_company_range_schema,
)
