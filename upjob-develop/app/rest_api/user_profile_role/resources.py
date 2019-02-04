from flask_restful import Resource, marshal_with

from rest_api.user_profile_role.items import UserProfileRole
from rest_api.user_profile_role.schemas import user_profile_role_schema


class UserProfileRoleResource(Resource):
    """Represent  userprofileroles.
    """

    @marshal_with(user_profile_role_schema)
    def get(self):
        user_profile_roles = UserProfileRole.get_all_user_profile_roles()
        return user_profile_roles, 200
