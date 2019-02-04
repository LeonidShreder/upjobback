from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.technology import Technology


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String)
    category_value = Column(String)
    technology_category = relationship("Technology")
