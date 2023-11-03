# schemas.py
from pydantic import BaseModel
from models import TransactionInfo
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateTransaction(BaseModel):
    name: str
    description: str
    amount: float
    currency: str

# TO support list and get APIs
class Transaction(CreateAndUpdateTransaction):
    id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedTransactionInfo(BaseModel):
    limit: int
    offset: int
    data: List[Transaction]
