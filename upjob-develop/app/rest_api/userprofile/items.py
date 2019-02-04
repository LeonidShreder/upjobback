from core.userprofile.userprofile_api import (
    create_user_profile,
    get_user_profile_by_id,
    get_user_profiles,
    update_user_profile,
)

from core.userprofile.validators import validate_user_profile_by_email


__all__ = [
    'UserProfile',
    'UserProfileInList',
]


class BaseUserProfile(object):
    """Represent base userprofile item.
    """
    def __init__(self, doc, role):
        self.id = str(doc.id)
        self.email = doc.email
        self.password = doc.password
        self.full_name = doc.full_name
        self.phone_number = doc.phone_number
        self.role = role
        self.company_id = doc.company_id


class UserProfileInList(BaseUserProfile):
    """Represent single userprofile item.
    """
    def __init__(self, doc, role):
        super(UserProfileInList, self).__init__(doc, role)

    @staticmethod
    def create_user_profile(args):
        doc = create_user_profile(args)
        return doc and UserProfileInList(doc, doc.role_id)

    @staticmethod
    def get_user_profiles(args):
        user_profile_list = get_user_profiles(args)
        return [UserProfileInList(u.UserProfile, u.UserProfileRole.role_value)
                for u in user_profile_list]


class UserProfile(BaseUserProfile):
    """Represent single userprofile item.
        """

    def __init__(self, doc, role):
        super(UserProfile, self).__init__(doc, role)

    @staticmethod
    def update_user_profile(user_profile_id, args):
        update_user_profile(user_profile_id, args)
        doc = get_user_profile_by_id(user_profile_id)
        return doc and UserProfile(doc.UserProfile,
                                   doc.UserProfileRole.role_value)

    @staticmethod
    def get_user_profile(user_profile_id):
        doc = get_user_profile_by_id(user_profile_id)
        return doc and UserProfile(doc.UserProfile,
                                   doc.UserProfileRole.role_value)

    @staticmethod
    def validate_user_profile_by_email(user_profile_id, email):
        return validate_user_profile_by_email(user_profile_id, email)
