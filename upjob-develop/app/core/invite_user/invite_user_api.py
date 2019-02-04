import ast

from core.email_worker import send_mail
from core.invite_user.validators import validate_user_profile_by_email
from core.utils import generate_password
from database import session
from models.userprofile import UserProfile


__all__ = [
    "create_user_profiles_from_invite",
]


def create_user_profiles_from_invite(args):
    user_list = []
    for key, value in ast.literal_eval(args['user_list']).items():
        if validate_user_profile_by_email(email=value['email']):
            return None
        user_list.append(UserProfile(email=value['email'],
                                     role_id=value['role'],
                                     password=generate_password(),
                                     company_id=args['company_id']))
    try:
        session.add_all(user_list)
        session.commit()
    except Exception as e:
        session.rollback()
    else:
        for user in user_list:
            send_mail(user.email, user.password)
        return user_list
