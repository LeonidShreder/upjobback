from flask_restful import Resource, marshal_with

from rest_api.quantity.items import Quantity
from rest_api.quantity.schemas import quantity_schema


class QuantityResource(Resource):
    """Represent  professions.
    """

    @marshal_with(quantity_schema)
    def get(self, company_id):
        quantity = Quantity.get_quantity_by_company_id(company_id)
        return quantity, 200
