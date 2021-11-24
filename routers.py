from fastapi import APIRouter, Depends, HTTPException
import pandas as pd
import requests
from config import USERNAME,TOKEN


router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.get('/{username}')
async def get_user_repos(username: str, limit: int = 10):
    return get_repo(username, limit)

def get_repo(url, limit):
    url = f"https://api.github.com/users/{url}/repos"
    dataframe = pd.DataFrame()
    page = 1
    while True:
        try:
            r = requests.get(url, auth=(USERNAME, TOKEN), params={"page":page})
            r.raise_for_status()
            assert len(r.json()) != 0
        except AssertionError:
            break
        except Exception as e:
            return e
        else:
            page += 1
            df = pd.json_normalize(r.json())
            dataframe = pd.concat([dataframe, df[["id", "name", "stargazers_count", "html_url"]]])
    return get_necessary_dataframe(dataframe, limit)

def get_necessary_dataframe(dataframe, limit):
    df = dataframe.rename(columns={'stargazers_count': "stars"})
    return df.sort_values(by=['stars', "name"], ascending=[False, True])[:limit].to_dict(orient='records')

