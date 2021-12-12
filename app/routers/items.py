from typing import Optional
from fastapi import FastAPI, BackgroundTasks, status
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

import os

from starlette.responses import JSONResponse
import motor.motor_asyncio

app = FastAPI()
router = APIRouter()

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_SAMPLE_URL"])
db = client.easywaldo

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
class Item(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    price: float
    isOffer: Optional[bool] = None
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

pre_db = [
   {"name": "waldo", "price": 10000, "isOffer": True},
   {"name": "mery", "price": 8000, "isOffer": True}
]

@router.get("/items")
def read_root():
    return pre_db

@router.get("/item/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@router.post("/item/create/")
async def create_item(createItemCommand: Item):
    item = jsonable_encoder(createItemCommand)
    newItem = await db["item"].insert_one(item)
    cretedItem = await db["item"].find_one({"_id": newItem.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=cretedItem)


@router.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@router.put("/item-update/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    update_item_encoded = jsonable_encoder(item)
    pre_db[item_id] = update_item_encoded
    return update_item_encoded


def write_notification(email: str, message=""):
    with open("email_log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)
    print('task completed')

@router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    print("routing cpmplted")
    return {"message": "Notification sent in the background"}