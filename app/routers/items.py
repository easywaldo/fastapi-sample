from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

app = FastAPI()
router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    isOffer: Optional[bool] = None

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

@router.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@router.put("/item-update/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    update_item_encoded = jsonable_encoder(item)
    pre_db[item_id] = update_item_encoded
    return update_item_encoded