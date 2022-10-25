import logging

from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(...)):
    if x_token != "run":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "sketch":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
