from sqlalchemy import Column, Integer, Date, Float, ForeignKey

from database import Base


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    expiration_date = Column(Date)
    sum = Column(Float)
    company_id = Column(Integer, ForeignKey('company.id'))
