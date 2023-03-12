import logging
from typing import Union

from fastapi import FastAPI, Query

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/webhook")
async def webhook(
    mode: str | None = Query(default=None, alias="hub.mode"),
    challenge: str | None = Query(default=None, alias="hub.challenge"),
    verify_token: str | None = Query(default=None, alias="hub.verify_token"),
):
    data = {
        "hub.mode": mode,
        "hub.challenge": challenge,
        "hub.verify_token": verify_token,
    }
    logger.info("Route=webhook with kwargs=%s", data)
    if mode == "subscribe":
        logger.info("Subscribe mode")
        return challenge
    return data
