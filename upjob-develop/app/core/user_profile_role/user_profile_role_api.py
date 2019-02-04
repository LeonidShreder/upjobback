from database import session
from models.user_profile_role import UserProfileRole

__all__ = [
    "get_user_profile_roles",
]


def get_user_profile_roles():
    return session.query(UserProfileRole).all()
