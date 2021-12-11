from typing import Optional
from fastapi import FastAPI
from fastapi import Depends, FastAPI
from app.routers import items, users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])

origins = [
    "https://hott.kr"
]

app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)