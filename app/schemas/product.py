from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
  name:str
  price:float
  quantity:int
  serial_number:str
  
class ProductCreate(ProductBase):
  pass

class ProductInfo(ProductBase):
  date_created:datetime
  in_stock:bool
  class Config:
    orm_mode = True

class ProductRead(ProductInfo):
  id:int
  class Config:
    orm_mode = True

class ProductPut(ProductBase):
  name:Optional[str]
  price:Optional[float]
  quantity:Optional[int]