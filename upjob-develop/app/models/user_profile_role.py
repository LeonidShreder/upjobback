from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base


class UserProfileRole(Base):
    __tablename__ = 'userprofilerole'

    id = Column(Integer, primary_key=True)
    role_name = Column(String)
    role_value = Column(String)
    role_user = relationship("UserProfile")
