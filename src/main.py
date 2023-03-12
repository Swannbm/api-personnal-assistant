import logging
from typing import Union

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/webhook")
async def webhook(
    hub_mode: str | None = None,
    hub_challenge: str | None = None,
    hub_verify_token: str | None = None,
):
    logger.info("Route=webhook with kwargs=%s", kwargs)
    if hub_mode == "subscribe":
        return hub_challenge
    return {
        "hub_mode": hub_mode,
        "hub_challenge": hub_challenge,
        "hub_verify_token": hub_verify_token,
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
