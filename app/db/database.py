import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# get Database URL From training server.
SQLALCHEMY_DATABASE_URL=os.environ['SQL_DATABASE_URLS']

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='utf-8'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
