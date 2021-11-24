from fastapi import Depends,FastAPI,HTTPException
import uvicorn

import routers

app = FastAPI()
app.include_router(routers.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)

