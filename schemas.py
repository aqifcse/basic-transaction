# schemas.py
from pydantic import BaseModel
import datetime
from models import TransactionInfo
from typing import Optional, List



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    password: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


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
