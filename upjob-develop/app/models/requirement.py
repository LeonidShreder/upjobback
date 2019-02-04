import enum
from sqlalchemy import Column, Integer, ForeignKey, Enum
from database import Base

class Requirement(Base):
    __tablename__ = 'requirement'

    id = Column(Integer, primary_key=True)
    technology_id = Column(Integer, ForeignKey('technology.id'))
    vacancy_id = Column(Integer, ForeignKey('vacancy.id'))
    experience_id = Column(Integer, ForeignKey('experience.id'))
