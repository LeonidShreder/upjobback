from flask_restful import Resource, abort, marshal_with

from core.invite_user.invite_user_api import create_user_profiles_from_invite
from .parsers import get_invite_user
from .schemas import invite_user_schema


class InviteUserResource(Resource):
    """
    Represent an user.
    """

    @marshal_with(invite_user_schema)
    def post(self):
        args = get_invite_user.parse_args()
        result = create_user_profiles_from_invite(args)
        if result is None:
            abort(400, message="Company cannot be created. Maybe some email is"
                               "already used.")
        return result, 201
