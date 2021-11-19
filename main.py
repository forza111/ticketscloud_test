from fastapi import Depends,FastAPI,HTTPException
import uvicorn

import routers
import asyncio
import time
from aiohttp import ClientSession, ClientResponseError

app = FastAPI()
app.include_router(routers.router)
URL = 'https://api.github.com/users/forza111'



async def fetch_url_data(session, url, params):
    try:
        async with session.get(url, params=params) as response:
            resp = await response.json()
            print(f'fetch_url_data success with params {params}')
    except Exception as e:
        raise Exception("%e has error '%s'" % (url, e))
    else:
        return resp


async def fetch_async(loop, pages):
    url = "https://api.github.com/users/forza111/repos"
    tasks = []
    async with ClientSession(headers=headers) as session:
        for p in range(pages-2,pages):
            params = {"per_page": 30, "page": p}
            task = asyncio.ensure_future(fetch_url_data(session, url, params))
            tasks.append(task)
        try:
            responses = await asyncio.gather(*tasks,return_exceptions=False)
            assert len(responses[0]) != 0
        except Exception as e:
            raise Exception("%e has error '%s'" % (url, e))
        else:
            return responses


if __name__ == '__main__':
    start_time = time.time()
    pages = 1
    while True:
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_async(loop, pages))
        try:
            loop.run_until_complete(future)
            responses = future.result()
            print(responses)
            pages += 5
        except Exception as e:
            print('e')
            break
    print(f'Запрос выполнен за {time.time() - start_time} секунд')









if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

