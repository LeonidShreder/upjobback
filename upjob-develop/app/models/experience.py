from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.competence import Competence
from models.requirement import Requirement


class Experience(Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    experience_name = Column(String)
    experience_value = Column(String)
    competence_experience = relationship("Competence")
    requirement_experience = relationship("Requirement")

