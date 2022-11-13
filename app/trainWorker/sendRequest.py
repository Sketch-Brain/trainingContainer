import logging
import os

import aiohttp
import json

logger = logging.getLogger("trainer")

async def sendResults(experimentId: str, accuracy):
    logger.info(f"Send_request : {experimentId}, accuracy : {accuracy}")
    urls = os.environ.get("RESULT_URLS")
    headers = { 'Content-Type':'application/json'}
    payloads = json.dumps({
        "uuid":experimentId,
        "result": str(accuracy)
    })
    async with aiohttp.ClientSession() as session:
        async with session.patch(url=urls, data=payloads, headers=headers) as response:
            logger.info(f"response http : {response.status}")
