from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DECIMAL, Boolean
from db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150))
    email = Column(String(150))
    password = Column(String(150))
    full_name = Column(String(150))
    disabled = Column(Boolean)

class TransactionInfo(Base):
    __tablename__ = "transaction_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True) 
    description = Column(String(200), index=True)
    amount = Column(DECIMAL(precision=10, scale=2)) 
    currency = Column(String(10), index=True)
