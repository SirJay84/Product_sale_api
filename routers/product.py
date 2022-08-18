from itertools import product
from sqlite3 import dbapi2
from unittest import skip
from fastapi import APIRouter,Depends,HTTPException
from typing import Dict,List,Generator
from sqlalchemy.orm import Session
from database.session import SessionLocal
from models.product import Product
from schemas.product import ProductRead,ProductCreate,ProductPut,ProductInfo

#Dependency Function
def get_db() -> Generator:
  try:
    db = SessionLocal()
    yield db
  finally:
    db.close()

product_router = APIRouter()

#Create Product:
@product_router.post('/',
response_model=ProductInfo,
summary='Create a product',
status_code=200)
def create_product(product:ProductCreate,db:Session=Depends(get_db)):
  db_product = db.query(Product).filter(Product.name==product.name).first()
  if db_product:
    raise HTTPException(status_code=400,detail='Sorry this product already exists!')
  db_product = Product(**product.dict())
  db.add(db_product)
  db.commit()
  db.refresh(db_product)
  return db_product

#Get all products:
@product_router.get('/',
response_model=List[ProductRead],
summary = 'Get all products',
status_code = 200)
def get_products(db:Session=Depends(get_db),skip:int=0,limit:int=10):
  products = db.query(Product).offset(skip).limit(limit).all()
  return products

#Get single product:
@product_router.get('/{productID}',
response_model=ProductInfo,
summary = 'Get a single product',
status_code = 200)
def get_product(productID:int,db:Session = Depends(get_db)):
  db_product = db.query(Product).filter(Product.id == productID).first()
  if db_product is None:
    raise HTTPException(status_code=404,detail='Sorry this product does not exist.')
  return db_product

#Update a product
@product_router.put('/{productID}',
response_model=Dict[str,str],
summary='Update a product',
status_code=200)
def update_product(productID:int, product:ProductPut, db:Session = Depends(get_db)):
  db_product = db.query(Product).filter(Product.id==productID).first()
  if db_product is None:
    raise HTTPException(status_code=404,detail='Sorry this product does not exist.')
  db_product.name = product.name
  db_product.price = product.price
  db_product.quantity = product.quantity
  db.commit()
  return {'message':'Product updated successfully.'}

#Delete Product:
@product_router.delete('/{productID}',
response_model=Dict[str,str],
summary = 'Delete a product',
status_code = 200)
def delete_product(productID:int,db:Session = Depends(get_db)):
  db_product=db.query(Product).filter(Product.id == productID).first()
  if db_product is None:
    raise HTTPException(status_code=404,detail='Sorry this product does not exist.')
  db.delete(db_product)
  db.commit()
  return{'message':'Product deleted successfully.'}



