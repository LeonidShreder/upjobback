from sqlalchemy import update as upd

from core.decorators import create, update
from database import session
from models.user_profile_role import UserProfileRole
from models.userprofile import UserProfile


__all__ = [
    "create_user_profile",
    "get_user_profiles",
    "get_user_profile_by_id",
    "update_user_profile",
]


@create
def create_user_profile(args):
    return UserProfile(**args)


def get_user_profiles(args):
    return session.query(UserProfile, UserProfileRole).filter_by(**args).join(
        UserProfileRole, UserProfileRole.id == UserProfile.role_id
    ).all()


def get_user_profile_by_id(user_profile_id):
    return session.query(UserProfile, UserProfileRole).join(
        UserProfileRole, UserProfileRole.id == UserProfile.role_id
    ).filter(UserProfile.id == user_profile_id).first()


@update
def update_user_profile(user_profile_id, args):
    return upd(UserProfile).where(
        UserProfile.id == user_profile_id).values(**args)
