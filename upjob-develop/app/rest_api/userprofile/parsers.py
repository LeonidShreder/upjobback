from flask_restful.reqparse import RequestParser

post_user_profile_parser = RequestParser()
post_user_profile_parser.add_argument('email', required=True)
post_user_profile_parser.add_argument('password', required=True)
post_user_profile_parser.add_argument('full_name', required=True)
post_user_profile_parser.add_argument('phone_number', required=True)
post_user_profile_parser.add_argument('role_id', required=True)
post_user_profile_parser.add_argument('company_id', required=True)

get_user_profile_parser = RequestParser()
get_user_profile_parser.add_argument('email', store_missing=False)
get_user_profile_parser.add_argument('password', store_missing=False)
get_user_profile_parser.add_argument('full_name', store_missing=False)
get_user_profile_parser.add_argument('phone_number', store_missing=False)
get_user_profile_parser.add_argument('role_id', store_missing=False)
get_user_profile_parser.add_argument('company_id', store_missing=False)
