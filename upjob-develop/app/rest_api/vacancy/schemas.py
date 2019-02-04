from flask_restful import fields

__all__ = {
    'vacancy_card_schema',
    'vacancy_list_schema',
}

nested_requirement_schema = dict(
    id=fields.String,
    name=fields.String,
    experience=fields.String,
)

base_vacancy_schema = dict(
    id=fields.String,
    title=fields.String,
    description=fields.String,
    user_id=fields.String,
    is_activated=fields.String,
    price=fields.String,
    profession=fields.String,
    company=fields.String,
    requirements=fields.List(fields.Nested(nested_requirement_schema)),
)

vacancy_list_schema = dict(
    id=base_vacancy_schema["id"],
    title=base_vacancy_schema["title"],
    price=base_vacancy_schema["price"],
    profession=base_vacancy_schema["profession"],
    is_activated=base_vacancy_schema["is_activated"],
    company=base_vacancy_schema["company"],
    requirements=base_vacancy_schema["requirements"],
)

vacancy_card_schema = dict(
    base_vacancy_schema,
)
