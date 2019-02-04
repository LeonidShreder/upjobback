from flask_restful.reqparse import RequestParser

post_company_parser = RequestParser()
post_company_parser.add_argument('title', type=str, required=True)
post_company_parser.add_argument('address', type=str, required=True)
post_company_parser.add_argument('description', required=True)
post_company_parser.add_argument('size_range_id', required=True)
post_company_parser.add_argument('phone_number', required=True)
post_company_parser.add_argument('email', required=True)

get_company_parser = RequestParser()
get_company_parser.add_argument('title', store_missing=False)
get_company_parser.add_argument('address', store_missing=False)
get_company_parser.add_argument('description', store_missing=False)
get_company_parser.add_argument('size_range_id', store_missing=False)
get_company_parser.add_argument('phone_number', store_missing=False)
get_company_parser.add_argument('email', store_missing=False)
