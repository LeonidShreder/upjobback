import json
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


with open(os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'config/config.json', ))) as f:
    config = json.load(f)

engine = create_engine('postgresql://{}:{}@localhost/{}'.format(
    config["db_user"], config["db_user_password"], config["db_name"]),
    echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


def init_db():
    from models.userprofile import UserProfile
    from models.company import Company
    from models.technology import Technology
    from models.requirement import Requirement
    from models.competence import Competence
    from models.employee import Employee
    from models.vacancy import Vacancy
    from models.purchase import Purchase
    from models.profession import Profession
    from models.experience import Experience
    from models.user_profile_role import UserProfileRole
    from models.company_range import CompanyRange
    from models.category import Category
    Base.metadata.create_all(bind=engine)
