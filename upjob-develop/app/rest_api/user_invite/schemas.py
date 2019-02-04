from flask_restful import fields

__all__ = [
    'invite_user_schema',
]

base_invite_user_schema = dict(
    id=fields.String,
    email=fields.String,
    password=fields.String,
    role_id=fields.String,
)

invite_user_schema = dict(
    base_invite_user_schema,
)
