from sqlalchemy import Column, Integer, String,DateTime,func,Float,ForeignKey
from sqlalchemy.orm import relationship
from database.base_class import Base

class Sales(Base):
  __tablename__ = 'sales'
  id = Column(Integer, primary_key=True)
  description = Column(String, nullable=False)
  quantity = Column(Integer, nullable=False)
  price = Column(Float, nullable=False)
  sales_date = Column(DateTime(timezone=False), server_default=func.now())
  product_id = Column(String,ForeignKey('products.id'), nullable=False)
  products = relationship('Product', back_populates='sales')

def __repr__(self):
  return "<Sales '{}'>".format(self.description)