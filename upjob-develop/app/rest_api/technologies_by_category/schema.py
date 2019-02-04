from flask_restful import fields

__all__ = {
    'filters_schema',
}

nested_technology_schema = dict(
    id=fields.String,
    name=fields.String,
)

base_filter_schema = dict(
    category=fields.String,
    technology=fields.List(fields.Nested(nested_technology_schema))
)

filters_schema = dict(
    base_filter_schema
)
