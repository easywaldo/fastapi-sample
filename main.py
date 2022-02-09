from typing import Optional
from fastapi import FastAPI
from fastapi import Depends, FastAPI
from app.routers import items, users, lectures, token
import uvicorn

app = FastAPI(debug=True)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(lectures.router, prefix="/items", tags=["items"])
app.include_router(token.router, prefix="/token", tags=["token"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
