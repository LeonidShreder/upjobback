from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.employee import Employee
from models.vacancy import Vacancy


class UserProfile(Base):
    __tablename__ = 'userprofile'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    phone_number = Column(String)
    role_id = Column(Integer, ForeignKey('userprofilerole.id'))
    company_id = Column(Integer, ForeignKey('company.id'))
    employee = relationship("Employee", viewonly=True)
    vacancy = relationship("Vacancy", viewonly=True)
