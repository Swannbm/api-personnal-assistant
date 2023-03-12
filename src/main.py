from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/webhook")
async def webhook(**kwargs):
    mode = kwargs.get("hub.mode")
    if mode == "subscribe":
        challenge = kwargs.get("hub.challenge")
        return challenge
    return kwargs


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
