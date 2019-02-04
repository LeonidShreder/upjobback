from core.userprofile.userprofile_api import get_user_profiles


__all__ = [
    "validate_user_profile_by_email",
]


def validate_user_profile_by_email(user_profile_id, email):
    return len(set(get_user_profiles({'email': email})).difference(
        get_user_profiles({'id': user_profile_id}))) > 0
