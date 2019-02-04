from flask_restful.reqparse import RequestParser


get_invite_user = RequestParser()
get_invite_user.add_argument('user_list', required=True)
get_invite_user.add_argument('company_id', required=True)
