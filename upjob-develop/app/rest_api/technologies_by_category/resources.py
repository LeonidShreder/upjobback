from flask_restful import Resource, marshal_with

from rest_api.technologies_by_category.schema import filters_schema
from rest_api.technologies_by_category.items import TechnologiesByCategory


class TechnologiesByCategoryRecource(Resource):
    """
    Represent list with technologies_by_category.
    """

    @marshal_with(filters_schema)
    def get(self, **args):
        filter_list = TechnologiesByCategory.get_technologies_by_category(**args)
        return filter_list, 200
