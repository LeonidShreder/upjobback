from core.invite_user.invite_user_api import create_user_profiles_from_invite


__all__ = [
    'InviteUser',
]


class BaseInviteUser(object):
    """Represent base user item.
    """
    def __init__(self, doc):
        self.id = str(doc.id)
        self.email = doc.email
        self.password = doc.password
        self.role_id = doc.role_id


class InviteUser(BaseInviteUser):
    """Represent single user item.
    """
    def __init__(self, doc):
        super(InviteUser, self).__init__(doc)

    @staticmethod
    def create_company(args):
        doc = create_user_profiles_from_invite(args)
        return doc and InviteUser(doc)
