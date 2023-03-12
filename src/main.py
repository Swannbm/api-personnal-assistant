import logging
from typing import Dict

from fastapi import FastAPI, Query, Body

from .config import VERIFY_TOKEN

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/webhook")
async def subscribe(
    mode: str = Query(alias="hub.mode"),
    challenge: str = Query(alias="hub.challenge"),
    verify_token: str = Query(alias="hub.verify_token"),
):
    data = {
        "hub.mode": mode,
        "hub.challenge": challenge,
        "hub.verify_token": verify_token,
    }
    logger.info("Route=GET /webhook with paremeters=%s", data)
    if mode == "subscribe" and challenge and verify_token == VERIFY_TOKEN:
        logger.info("Subscribe mode")
        return int(challenge)
    return data


@app.post("/webhook")
async def webhook(payload: Dict = Body()):
    logger.info("Route=POST /webhook with payload=%s", payload)
    return {"payload": payload}
