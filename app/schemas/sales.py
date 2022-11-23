from pydantic import BaseModel
from typing import Optional,List
from datetime import datetime

class SalesBase(BaseModel):
  description:str
  quantity:int
  price:float
  
class SalesCreate(SalesBase):
  product_id:int

class SalesPut(SalesBase):
  description:Optional[str]
  quantity:Optional[int]
  price:Optional[int]

class SalesInfo(SalesBase):
  sales_date:datetime
  product_id:int
  class Config:
    orm_mode = True

class SalesRead(SalesInfo):
  id:int
  class Config:
    orm_mode = True
