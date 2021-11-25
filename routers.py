from fastapi import APIRouter, Depends, HTTPException
import pandas as pd
import requests
from requests.exceptions import HTTPError

from config import USERNAME,TOKEN


router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.get('/{username}')
async def get_user_repos(username: str):
    return get_repo(username)

def get_repo(URL):
    url = f"https://api.github.com/users/{URL}/repos"
    dataframe = pd.DataFrame()
    while True:
        try:
            page = 1
            r = requests.get(url, auth=(USERNAME, TOKEN), params={"page":page})
            r.raise_for_status()
            assert len(r.json()) != 0
        except AssertionError:
            break
        except HTTPError as http_err:
            status_code, detail = str(http_err).split(" ", 1)
            raise HTTPException(status_code=int(status_code), detail=detail)
        else:
            page += 1
            df = pd.json_normalize(r.json())
            dataframe = pd.concat([dataframe, df[["id", "name"]]])
    return dataframe[["id", "name"]].to_dict(orient='records')