from flask_restful import fields

__all__ = [
    'quantity_schema',
]

base_quantity_schema = dict(
    quantity=fields.Integer,
)

quantity_schema = dict(
    base_quantity_schema,
)
