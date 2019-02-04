from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.requirement import Requirement


class Vacancy(Base):
    __tablename__ = 'vacancy'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('userprofile.id'))
    is_activated = Column(Boolean)
    price = Column(Float)
    profession_id = Column(Integer, ForeignKey('profession.id'), )
    requirements = relationship("Requirement")
