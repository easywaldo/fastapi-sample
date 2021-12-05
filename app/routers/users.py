from typing import Optional
from datetime import date
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

userList = []

# Declare a variable as a str
# and get editor support inside the function
def user(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    fullName: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    fullName: Optional[str] = None

@router.get("/users", tags=['users'])
async def read_root():
    return userList

@router.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    userList.append(user)
    return user
