from flask_restful import Resource, abort, marshal_with

from rest_api.userprofile.items import (
    UserProfile,
    UserProfileInList,
)
from rest_api.userprofile.parsers import (
    get_user_profile_parser,
    post_user_profile_parser,
)
from rest_api.userprofile.schemas import (
    user_profile_schema,
)


class UserProfileListResource(Resource):

    @marshal_with(user_profile_schema)
    def get(self):
        args = get_user_profile_parser.parse_args()
        user_profiles = UserProfileInList.get_user_profiles(args)
        return user_profiles, 200

    @marshal_with(user_profile_schema)
    def post(self):
        args = post_user_profile_parser.parse_args()
        # TODO: validate if this company already exists
        result = UserProfileInList.create_user_profile(args)
        if result is None:
            abort(400, message="User profile cannot be created")
        return result, 201


class UserProfileResource(Resource):

    @marshal_with(user_profile_schema)
    def get(self, user_profile_id):
        user_profile = UserProfile.get_user_profile(user_profile_id)
        return user_profile, 200

    @marshal_with(user_profile_schema)
    def put(self, user_profile_id):
        args = get_user_profile_parser.parse_args()
        if UserProfile.validate_user_profile_by_email(user_profile_id,
                                                      args.get('email')):
            abort(400, message="Email is already used")
        user_profile = UserProfile.update_user_profile(user_profile_id, args)
        return user_profile, 200
