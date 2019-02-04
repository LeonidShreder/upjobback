from database import session
from models.profession import Profession

__all__ = [
    "get_professions",
]


def get_professions():
    return session.query(Profession).all()
