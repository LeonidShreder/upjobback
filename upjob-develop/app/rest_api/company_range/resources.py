from flask_restful import Resource, marshal_with

from rest_api.company_range.items import CompanyRangeList
from rest_api.company_range.schemas import company_range_schema


class CompanyRangeResource(Resource):
    """Represent  ranges.
    """

    @marshal_with(company_range_schema)
    def get(self):
        ranges = CompanyRangeList.get_all_ranges()
        return ranges, 200
