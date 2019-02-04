from flask_restful import fields

__all__ = [
    'user_profile_role_schema',
]

base_user_profile_role_schema = dict(
    id=fields.String,
    name=fields.String,
    value=fields.String,
)

user_profile_role_schema = dict(
    base_user_profile_role_schema,
)
