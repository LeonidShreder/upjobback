from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.competence import Competence
from models.requirement import Requirement


class Technology(Base):
    __tablename__ = 'technology'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    competence = relationship("Competence")
    requirements = relationship("Requirement")
