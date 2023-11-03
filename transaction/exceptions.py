# exceptions.py
class TransactionInfoException(Exception):
    ...


class TransactionInfoNotFoundError(TransactionInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Transaction Info Not Found"


class TransactionInfoInfoAlreadyExistError(TransactionInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Transaction Info Already Exists"
