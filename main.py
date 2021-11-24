from fastapi import Depends,FastAPI,HTTPException
import uvicorn

import routers
import asyncio
import time
from aiohttp import ClientSession, ClientResponseError
from config import HEADERS

app = FastAPI()
app.include_router(routers.router)
URL = 'https://api.github.com/users/forza111'


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

