from core.userprofile.userprofile_api import get_user_profiles


__all__ = [
    "validate_user_profile_by_email",
]


def validate_user_profile_by_email(email):
    return len(set(get_user_profiles({'email': email}))) > 0
