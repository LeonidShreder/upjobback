from core.user_profile_role.user_profile_role_api import (
    get_user_profile_roles,
)

__all__ = [
    'UserProfileRole',
]


class BaseUserProfileRole(object):
    """Represent base userprofilerole item.
    """
    def __init__(self, doc):
        self.id = str(doc.id)
        self.name = str(doc.role_name)
        self.value = str(doc.role_value)


class UserProfileRole(BaseUserProfileRole):

    def __init__(self, doc):
        super(UserProfileRole, self).__init__(doc)

    @staticmethod
    def get_all_user_profile_roles():
        user_profile_role_list = get_user_profile_roles()
        return [UserProfileRole(c) for c in user_profile_role_list]
