from flask_restful import fields

__all__ = [
    'profession_schema',
]

base_profession_schema = dict(
    id=fields.String,
    name=fields.String,
    value=fields.String,
)

profession_schema = dict(
    base_profession_schema,
)
