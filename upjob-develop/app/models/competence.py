from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class Competence(Base):
    __tablename__ = 'competence'

    id = Column(Integer, primary_key=True)
    technology_id = Column(Integer, ForeignKey('technology.id'))
    employee_id = Column(Integer, ForeignKey('employee.id'))
    experience_id = Column(Integer, ForeignKey('experience.id'))
