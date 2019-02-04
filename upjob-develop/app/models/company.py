from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from models.userprofile import UserProfile
from models.purchase import Purchase


class Company(Base):
    __tablename__ = 'company'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    title = Column(String)
    address = Column(String)
    description = Column(String)
    size_range_id = Column(Integer, ForeignKey('companyrange.id'))
    phone_number = Column(String)
    email = Column(String)
    user_profile = relationship('UserProfile', viewonly=True)
    purchases = relationship('Purchase', viewonly=True)
