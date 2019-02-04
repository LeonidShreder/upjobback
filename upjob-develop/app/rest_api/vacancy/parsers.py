from flask_restful.reqparse import RequestParser


get_vacancy_parser = RequestParser()
get_vacancy_parser.add_argument('title', store_missing=False)
get_vacancy_parser.add_argument('description', store_missing=False)
get_vacancy_parser.add_argument('user_id', store_missing=False)
get_vacancy_parser.add_argument('is_activated', store_missing=False)
get_vacancy_parser.add_argument('price', store_missing=False)
get_vacancy_parser.add_argument('value', store_missing=False, action='append')
get_vacancy_parser.add_argument('technologies', store_missing=False,
                                action='append')

put_vacancy_parser = RequestParser()
put_vacancy_parser.add_argument('id', store_missing=False)
put_vacancy_parser.add_argument('title', store_missing=False)
put_vacancy_parser.add_argument('description', store_missing=False)
put_vacancy_parser.add_argument('user_id', store_missing=False)
put_vacancy_parser.add_argument('is_activated', store_missing=False)
put_vacancy_parser.add_argument('price', store_missing=False)
put_vacancy_parser.add_argument('value', store_missing=False)
put_vacancy_parser.add_argument('technologies', store_missing=False,
                                action='append')
