from datetime import date
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Declare a variable as a str
# and get editor support inside the function
def user(user_id: str):
    return user_id


# A Pydantic model
class User(BaseModel):
    id: int
    name: str
    joined: date


@router.get("/users", tags=['users'])
async def read_root():
    my_user: User = User(id=3, name="John Doe", joined="2018-07-19")

    second_user_data = {
        "id": 4,
        "name": "Mary",
        "joined": "2018-11-30",
    }

    my_second_user: User = User(**second_user_data)
    return my_second_user