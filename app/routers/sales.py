from fastapi import APIRouter,Depends,HTTPException
from typing import Dict,List,Generator
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.sales import Sales
from app.schemas.sales import SalesCreate, SalesInfo,SalesPut,SalesRead

# Dependency Function:
def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

sales_router = APIRouter()

#list of all sales:
@sales_router.get('/',
response_model=List[SalesRead],
status_code=200,
summary='List of all Sales')
def all_sales(db:Session=Depends(get_db),skip:int=0,limit:int=10):
  sales = db.query(Sales).offset(skip).limit(limit).all()
  return sales

#Get a sale:
@sales_router.get('/{salesID}',
response_model=SalesInfo,
status_code=200,
summary='Get a sale item')
def get_sale(salesID:int, db:Session=Depends(get_db)):
  sales_item = db.query(Sales).filter(Sales.id ==salesID).first()
  if sales_item is None:
    raise HTTPException(status_code=404, detail='Sorry this sale does not exist.')
  return sales_item

#Create a new sale:
@sales_router.post('/',
response_model=SalesInfo,
status_code=200,
summary='Add a new sale')
def create_sale(sales:SalesCreate,db:Session=Depends(get_db)):
  new_sale = Sales(**sales.dict())
  db.add(new_sale)
  db.commit()
  db.refresh(new_sale)
  return new_sale

#Update a sale:
@sales_router.put('/{salesID}',
response_model=Dict[str,str],
summary='Update a sale',
status_code=200)
def update_sale(salesID:int, sales:SalesPut, db:Session=Depends(get_db)):
  sales_item = db.query(Sales).filter(Sales.id ==salesID).first()
  if sales_item is None:
    raise HTTPException(status_code=404, detail='Sorry this sale does not exist.')
  sales_item.description = sales.description
  sales_item.quantity = sales.quantity
  sales_item.price = sales.price
  db.commit()
  return {'message':'Sale updated successfully.'}

#Delete a sale:
@sales_router.delete('/{salesID}',
response_model=Dict[str,str],
summary='Delete a sale',
status_code=200)
def delete_sale(salesID:int,db:Session=Depends(get_db)):
  sales_item = db.query(Sales).filter(Sales.id ==salesID).first()
  if sales_item is None:
    raise HTTPException(status_code=404, detail='Sorry this sale does not exist.')
  db.delete(sales_item)
  db.commit()
  return {'message':'Sale deleted successfully.'}
