# crud.py
from typing import List
from sqlalchemy.orm import Session
from exceptions import TransactionInfoInfoAlreadyExistError, TransactionInfoNotFoundError
from models import TransactionInfo
from schemas import CreateAndUpdateTransaction


# Function to get list of car info
def get_all_transactions(session: Session, limit: int, offset: int) -> List[TransactionInfo]:
    return session.query(TransactionInfo).offset(offset).limit(limit).all()


# Function to  get info of a particular transaction
def get_transaction_info_by_id(session: Session, _id: int) -> TransactionInfo:
    transaction_info = session.query(TransactionInfo).get(_id)

    if transaction_info is None:
        raise TransactionInfoNotFoundError

    return transaction_info


# Function to add a new transaction info to the database
def create_transaction(session: Session, transaction_info: CreateAndUpdateTransaction) -> TransactionInfo:
    transaction_details = session.query(TransactionInfo).filter(TransactionInfo.name == transaction_info.name).first()
    if transaction_details is not None:
        raise TransactionInfoInfoAlreadyExistError

    new_transaction_info = TransactionInfo(**transaction_info.dict())
    session.add(new_transaction_info)
    session.commit()
    session.refresh(new_transaction_info)
    return new_transaction_info


# Function to update details of the transaction
def update_transaction_info(session: Session, _id: int, info_update: CreateAndUpdateTransaction) -> TransactionInfo:
    transaction_info = get_transaction_info_by_id(session, _id)

    if transaction_info is None:
        raise TransactionInfoNotFoundError

    transaction_info.name = info_update.name
    transaction_info.description = info_update.description
    transaction_info.amount = info_update.amount
    transaction_info.currency = info_update.currency

    session.commit()
    session.refresh(transaction_info)

    return transaction_info


# Function to delete a transaction info from the db
def delete_transaction_info(session: Session, _id: int):
    transaction_info = get_transaction_info_by_id(session, _id)

    if transaction_info is None:
        raise TransactionInfoNotFoundError

    session.delete(transaction_info)
    session.commit()

    return