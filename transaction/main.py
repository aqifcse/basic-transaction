from fastapi import FastAPI, APIRouter, status

app = FastAPI()
router = APIRouter()


@router.get('/')
def get_transactions():
    return "return a list of transaction items"


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_transactions():
    return "create transaction item"


@router.patch('/{transactionId}')
def update_transaction(transactionId: str):
    return f"update transaction transaction with id {transactionId}"


@router.get('/{transactionId}')
def get_transaction(transactionId: str):
    return f"get transaction item with id {transactionId}"


@router.delete('/{transactionId}')
def delete_transaction(transactionId: str):
    return f"delete transaction item with id {transactionId}"


app.include_router(router, tags=['Transactions'], prefix='/api/transactions')


@app.get("/api/transaction")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}

