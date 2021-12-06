from typing import Optional
from datetime import datetime
from fastapi import Body, APIRouter
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()

userList = []

# Declare a variable as a str
# and get editor support inside the function
def user(user_id: str):
    return user_id


# A Pydantic model
class User:
    seq: int
    name: str
    joined: datetime
    tags: list
    def __init__(self, seq, name, joined, tags):
        self.seq = seq
        self.name = name
        self.joined = joined
        self.tags = tags

class UserIn(BaseModel):
    userName: str
    password: str = Field(None, title="passworld", min_length=10)
    email: EmailStr
    age: int = Field(None, title="age", gt=18)
    fullName: Optional[str] = None
    tags: list = []

class UserOut(BaseModel):
    userName: str
    email: EmailStr
    fullName: Optional[str] = None

@router.get("/users", tags=['users'])
async def read_root():
    return userList

@router.post("/user/", response_model=UserOut, status_code=201)
async def create_user(user: UserIn = Body(...,
    examples={
        "normal": {
            "surmmary": "a normal example",
            "description": "correct sample",
            "value": {    
                "userName": "easywaldo",
                "password": "mypassword",
                "email": "tester@gmail.com",
                "age": 20,
                "fullName": "easywaldo",
                "tags": ["python", "c#", "java", "go", "php", "javascript", "typescript", "elastic search"]
            }
        },
        "converted": {
            "surmmary": "a converted example",
            "description": "converted sample",
            "value": {    
                "userName": "easywaldo",
                "password": "mypassword",
                "email": "tester@gmail.com",
                "age": 20,
                "fullName": "easywaldo",
                "tags": []
            }
        },
        "invalid": {
            "surmmary": "a invalid example",
            "description": "invalid sample",
            "value": {    
                "userName": "easywaldo",
                "password": "12",
                "email": "tester@gmail.com",
                "age": 5,
                "fullName": "easywaldo",
                "tags": []
            }
        }
    })):
    userList.append(User(
        len(userList), user.userName, datetime.now(tz=None), user.tags))
    return user

@router.delete("/user/{userSeq}")
async def delete_user(userSeq: int):
    if (userList == []):
        return "empty"
    userList.remove(userList[userSeq])
    return "removed"

@router.put("/user/{userSeq}/update")
async def update_user(userSeq: int, user: UserIn):
    userList[userSeq].email = user.email
    userList[userSeq].tags = user.tags