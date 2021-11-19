import asyncio

from fastapi import APIRouter, Depends, HTTPException
import requests

router = APIRouter(
    prefix="/user",
    tags=["users"]
)
URL = "https://github.com/"

@router.get('/')
def main():
    task()

def task():
    r = requests.get(URL)
    return r.content