from flask_restful.reqparse import RequestParser


get_employee_parser = RequestParser()
get_employee_parser.add_argument('title', store_missing=False)
get_employee_parser.add_argument('full_name', store_missing=False)
get_employee_parser.add_argument('user_id', store_missing=False)
get_employee_parser.add_argument('public_id', store_missing=False)
get_employee_parser.add_argument('portfolio', store_missing=False)
get_employee_parser.add_argument('is_activated', store_missing=False)
get_employee_parser.add_argument('value', store_missing=False, action='append')
get_employee_parser.add_argument('competence', store_missing=False)
get_employee_parser.add_argument('technologies', store_missing=False,
                                 action='append')

put_employee_parser = RequestParser()
put_employee_parser.add_argument('id', store_missing=False)
put_employee_parser.add_argument('title', store_missing=False)
put_employee_parser.add_argument('full_name', store_missing=False)
put_employee_parser.add_argument('user_id', store_missing=False)
put_employee_parser.add_argument('public_id', store_missing=False)
put_employee_parser.add_argument('portfolio', store_missing=False)
put_employee_parser.add_argument('is_activated', store_missing=False)
put_employee_parser.add_argument('value', store_missing=False)
put_employee_parser.add_argument('competence', store_missing=False)
put_employee_parser.add_argument('technologies', store_missing=False,
                                 action='append')
