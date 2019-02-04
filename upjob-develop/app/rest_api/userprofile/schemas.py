from flask_restful import fields

__all__ = [
    'user_profile_schema',
]

base_user_profile_schema = dict(
    id=fields.String,
    email=fields.String,
    password=fields.String,
    full_name=fields.String,
    phone_number=fields.String,
    role=fields.String,
    company_id=fields.String,
)

user_profile_schema = dict(
    base_user_profile_schema,
)
