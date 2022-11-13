import logging
import os
import requests
import aiohttp
import json

logger = logging.getLogger("trainer")

async def sendResults(userId:str, experimentId: str, accuracy):
    logger.info(f"Send_request : {experimentId}, accuracy : {accuracy}")
    urls = os.environ.get("RESULT_URLS")
    resultUrls = urls + "/api/server/result"
    headers = { 'Content-Type':'application/json'}
    payloads = json.dumps({
        "uuid":experimentId,
        "result": str(accuracy)
    })
    async with aiohttp.ClientSession() as session:
        async with session.patch(url=resultUrls, data=payloads, headers=headers) as response:
            logger.info(f"response http : {response.status}")


async def sendFiles(userId: str, experimentId: str):
    urls = os.environ.get("RESULT_URLS")

    with open("app/trainWorker/model.py", "rb") as file: #Read as bin
        binResult = file.read()

    fileUrls = urls + "/api/file/model"

    payload = {
        "user":userId
    }
    files = [
        ('file', (experimentId[:6]+"model.py", binResult, 'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("PUT", fileUrls, headers=headers, data=payload, files=files)
    logger.info(f"response : {response.status_code}")
    logger.info(f"{response}")
