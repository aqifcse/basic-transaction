from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from transaction import get_all_transactions, create_transaction, get_transaction_info_by_id, update_transaction_info, delete_transaction_info
from db import get_db
from exceptions import TransactionInfoException
from schemas import Transaction, CreateAndUpdateTransaction, PaginatedTransactionInfo

router = APIRouter()


# Example of Class based view
@cbv(router)
class Transactions:
    session: Session = Depends(get_db)

    # API to get the list of transaction info
    @router.get("/transactions", response_model=PaginatedTransactionInfo)
    def list_transactions(self, limit: int = 10, offset: int = 0):

        transactions_list = get_all_transactions(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": transactions_list}

        return response

    # API endpoint to add a transaction info to the database
    @router.post("/transactions")
    def add_transaction(self, transaction_info: CreateAndUpdateTransaction):

        try:
            transaction_info = create_transaction(self.session, transaction_info)
            return transaction_info
        except TransactionInfoException as cie:
            raise HTTPException(**cie.__dict__)


# API endpoint to get info of a particular transaction
@router.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction_info(transaction_id: int, session: Session = Depends(get_db)):

    try:
        transaction_info = get_transaction_info_by_id(session, transaction_id)
        return transaction_info
    except TransactionInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to update a existing transaction info
@router.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: int, new_info: CreateAndUpdateTransaction, session: Session = Depends(get_db)):

    try:
        transaction_info = update_transaction_info(session, transaction_id, new_info)
        return transaction_info
    except TransactionInfoException as cie:
        raise HTTPException(**cie.__dict__)


# API to delete a transaction info from the data base
@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, session: Session = Depends(get_db)):

    try:
        return delete_transaction_info(session, transaction_id)
    except TransactionInfoException as cie:
        raise HTTPException(**cie.__dict__)