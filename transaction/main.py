from fastapi import FastAPI
from pydantic import BaseModel
from db import create_tables
import uvicorn
import api

# Initialize the app
app = FastAPI()

app.include_router(api.router)


@app.on_event("startup")
def on_startup():
    create_tables()


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to Towfiq's Transaction App"}

