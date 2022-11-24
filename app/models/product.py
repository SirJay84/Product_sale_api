from sqlalchemy import Column, Integer, String, Float,Boolean,DateTime,func
from sqlalchemy.orm import relationship
from app.database.base_class import Base

class Product(Base):
  __tablename__ = 'products'
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False, unique=True)
  price = Column(Float, nullable=False)
  quantity = Column(Integer, nullable=False)
  in_stock = Column(Boolean, nullable=False, default=True)
  serial_number = Column(String, nullable=False, unique=True)
  date_created = Column(DateTime(timezone=False), server_default=func.now())
  sales = relationship('Sales', back_populates='products')

  def __repr__(self):
    return "<Product '{}','{}'>".format(self.name,self.price)
