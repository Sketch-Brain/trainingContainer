import logging

logger = logging.getLogger("trainer")


async def injectLayer(runnable):
    with open("app/trainWorker/model.py", "rt") as file:
        reads = file.read()

    with open("app/trainWorker/model.py", "wt") as file:
        reads = reads.replace("#### LAYER DATA ###", runnable)
        file.write(reads)

    logger.info(f"reads: {reads}")
