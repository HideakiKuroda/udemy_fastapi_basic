from fastapi import FastAPI
from routers import contact


# class FastAPI を instance　化する
app = FastAPI()

# @app.get("/")  #　デコレーター
# async def read_root():    # async をつけて非同期関数にするのが基本
#     return {"Hello": "World"}

app.include_router(contact.router)