from fastapi import APIRouter
from.product import product_router
from.sales import sales_router

router = APIRouter()

router.include_router(product_router, prefix='/products', tags=['PRODUCT'])
router.include_router(sales_router, prefix='/sales', tags=['SALES'])