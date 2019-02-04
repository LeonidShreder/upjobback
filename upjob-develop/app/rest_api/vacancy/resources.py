from flask_restful import Resource, abort, marshal_with

from rest_api.vacancy.items import VacancyCard, VacancyInList
from rest_api.vacancy.schemas import vacancy_card_schema, vacancy_list_schema
from rest_api.vacancy.parsers import get_vacancy_parser, put_vacancy_parser


class VacancyListResource(Resource):
    """
    Represent vacancy list.
    """

    @marshal_with(vacancy_list_schema)
    def get(self):
        args = get_vacancy_parser.parse_args()
        vacancy_list = VacancyInList.get_vacancy_items(args)
        return vacancy_list, 200


class VacancyResource(Resource):
    """
    Represent vacancy card.
    """

    @marshal_with(vacancy_card_schema)
    def get(self, vacancy_id):
        vacancy = VacancyCard.get_vacancy(vacancy_id)
        if vacancy:
            return vacancy, 200
        else:
            abort(404, message="Employee not found")

    @marshal_with(vacancy_card_schema)
    def put(self):
        args = put_vacancy_parser.parse_args()
        vacancy = VacancyCard.put_vacancy(args)
        if vacancy:
            return vacancy, 200
        else:
            abort(404, message="Employee not found")
