from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://aqif:12345678@db:3306/transaction"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=db_engine)

def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()