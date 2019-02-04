from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.competence import Competence
from models.user_profile_role import UserProfileRole


class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String)
    full_name = Column(String)
    user_id = Column(Integer, ForeignKey('userprofile.id'))
    public_id = Column(Integer)
    portfolio = Column(String)
    is_activated = Column(Boolean)
    profession_id = Column(Integer, ForeignKey('profession.id'))
    competence = relationship("Competence")
