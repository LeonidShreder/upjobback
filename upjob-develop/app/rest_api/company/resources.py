from flask_restful import Resource, abort, marshal_with

from rest_api.company.items import Company, CompanyInList
from rest_api.company.parsers import get_company_parser, post_company_parser
from rest_api.company.schemas import company_list_schema, company_schema


class CompanyListResource(Resource):
    """Represent company list.
    """

    @marshal_with(company_list_schema)
    def get(self):
        args = get_company_parser.parse_args()
        companies = CompanyInList.get_all(args)
        return companies, 200

    @marshal_with(company_schema)
    def post(self):
        args = post_company_parser.parse_args()
        if Company.validate_company_by_email(args.get('email')):
            abort(400, message="Email is already used")
        result = Company.create_company(args)
        if result is None:
            abort(400, message="Company cannot be created")
        return result, 201


class CompanyResource(Resource):

    @marshal_with(company_schema)
    def get(self, company_id):
        company = Company.get_company(company_id)
        return company, 200

    @marshal_with(company_schema)
    def delete(self, company_id):
        company = Company.delete_company(company_id)
        return company, 204

    @marshal_with(company_schema)
    def put(self, company_id):
        args = get_company_parser.parse_args()
        company = Company.update_company(company_id, args)
        return company, 200
