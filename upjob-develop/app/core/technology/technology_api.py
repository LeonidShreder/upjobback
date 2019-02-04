from database import session
from models.technology import Technology
from models.category import Category


def get_technologies():
    return session.query(Technology, Category).join(
        Category, Category.id == Technology.category_id).all()
