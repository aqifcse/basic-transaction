import bcrypt
from fastapi import APIRouter

#the following line of code are to import the user in our model and schema
from models import User as ModelUser
from schemas import User
from schemas import User as Users
from db import SessionLocal

# Dependency

db = SessionLocal()
    

router = APIRouter()

@router.post("/register", response_model=Users)
async def create_user(user: User):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user = ModelUser(username=user.username, email=user.email, password=hashed_password, full_name=user.full_name, disabled=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user