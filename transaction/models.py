from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Decimal
from database import Base
import enum

class TransactionInfo(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String) 
    description = Column(String)
    amount = Column(Decimal(precision=10, scale=2)) 
    currency = Column(String)
