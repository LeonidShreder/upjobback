from flask_restful import fields

__all__ = [
    'employee_list_schema',
    'employee_schema',
]

nested_competence_schema = dict(
    id=fields.String,
    name=fields.String,
    experience=fields.String,
)

base_employee_schema = dict(
    id=fields.String,
    public_id=fields.String,
    is_activated=fields.String,
    title=fields.String,
    full_name=fields.String,
    user_id=fields.String,
    portfolio=fields.String,
    profession=fields.String,
    company=fields.String,
    competences=fields.List(fields.Nested(nested_competence_schema)),
)

employee_list_schema = dict(
    base_employee_schema,
)

employee_schema = dict(
    base_employee_schema,
)
