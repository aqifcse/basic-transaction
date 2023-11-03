from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DECIMAL
from db import Base

class TransactionInfo(Base):
    __tablename__ = "transaction_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True) 
    description = Column(String(200), index=True)
    amount = Column(DECIMAL(precision=10, scale=2)) 
    currency = Column(String(10), index=True)
