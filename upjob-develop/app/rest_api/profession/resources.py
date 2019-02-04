from flask_restful import Resource, marshal_with

from rest_api.profession.items import Profession
from rest_api.profession.schemas import profession_schema


class ProfessionResource(Resource):
    """Represent  professions.
    """

    @marshal_with(profession_schema)
    def get(self):
        professions = Profession.get_all_professions()
        return professions, 200
