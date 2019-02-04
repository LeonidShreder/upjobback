from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.employee import Employee
from models.vacancy import Vacancy


class Profession(Base):
    __tablename__ = 'profession'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(String)
    employee = relationship("Employee")
    vacancy = relationship("Vacancy")
