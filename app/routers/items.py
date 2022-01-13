from typing import Optional
from fastapi import FastAPI, Body, BackgroundTasks, status, HTTPException
from pydantic import BaseModel, Field
from bson import ObjectId
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder



import sqlalchemy as db
from sqlalchemy.sql.expression import select, text
from sqlalchemy.sql.schema import Sequence
engine = db.create_engine('mysql+pymysql://tester:test1234!$@127.0.0.1:3306/sample')
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (Table, Column, String, Integer, MetaData, select, func)
from flask_sqlalchemy import SQLAlchemy

Session = sessionmaker(bind = engine)

meta = MetaData()
lecture = Table(
   'lecture', meta, 
   Column('lecture_id', Integer, primary_key = True), 
   Column('lecture_name', String)
)
class Base(object):
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
    
db = SQLAlchemy()
class Lecture(db.Model):
    __tablename__ = 'lecture'
    lecture_name = Column(String(100))
    lecture_id = Column(Integer, primary_key=True, autoincrement = True)
    def __init__(self, lecture_name):
        self.lecture_name = lecture_name
            
    def __repr__(self):
        return "<Lecture(lectureName='%s')>" % (self.lecture_name)
        
session = Session()

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

class UpdateItem(BaseModel):
    name: Optional[str]
    price: float
    isOffer: Optional[bool] = None

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Easywaldo",
                "price": 10000,
                "isOffer": True
            }
        }

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

@router.delete("/item/{item_id}", response_description="delete item")
async def delete_item(id: str):
    delete_result = await db["item"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.put("/item/{item_id}")
def update_item(item_id: str, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@router.put("/item-update/{item_id}", response_model=Item)
async def update_item(item_id: str, item: UpdateItem = Body(...)):
    ##update_item_encoded = jsonable_encoder(item)
    ##pre_db[item_id] = update_item_encoded
    findItem = {k: v for k, v in item.dict().items() if v is not None}

    if len(findItem) >= 1:
        update_result = await db["item"].update_one({"_id": item_id}, {"$set": findItem})

        if update_result.modified_count == 1:
            if (
                updatedItem := await db["item"].find_one({"_id": item_id})
            ) is not None:
                return updatedItem

    if (existingItem := await db["item"].find_one({"_id": item_id})) is not None:
        return existingItem

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

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

@router.get("/lecture-list")
async def lecture_list():
    result = session.query(lecture).all()
    return result

@router.post("/lecture-create")
async def lecture_create(lectureName: str):
    lecture = Lecture(lectureName)
    session.add(lecture)
    session.commit()
    return True