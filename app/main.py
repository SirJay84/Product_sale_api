from fastapi import FastAPI
from app.routers.api import router
from app.database.session import engine
from app.database.base_class import Base

#Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
  title="Product Sale API",
  description="A Basic Product Sale Inventory API",
  version="0.1.0",
  docs_url="/developer/docs",
  redoc_url="/developer/redoc",
  contact={"name": "Jimmy","email":"jimbotela@icloud.com"}

)

@app.get('/', status_code=200, description='Home route')
def index():
  return {'message':'Hello Jimmy'}

#Instance of FastAPI:
app.include_router(router, responses={
  200: {'description': 'Ok'},
201: {'description': 'Created'},
202: {'description': 'Accepted'},
400: {"description": "Bad Request"},
401: {"description": "Unauthorized"},
403: {"description": "Forbidden"},
404: {"description": "Not found"},
405: {"description": "Method not allowed"}
})

