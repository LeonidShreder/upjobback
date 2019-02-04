from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from database import Base
from models.company import Company


class CompanyRange(Base):
    __tablename__ = 'companyrange'

    id = Column(Integer, primary_key=True)
    size_name = Column(String)
    size_value = Column(String)
    company_size = relationship("Company")
