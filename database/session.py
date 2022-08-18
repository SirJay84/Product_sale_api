from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/user/Documents/SirJayProjects/TechCamp/duka2.db'

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
