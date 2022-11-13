import logging
from app.crud import containerCRUD
import traceback

logger = logging.getLogger("trainer")


async def injectLayer(strExpId,experiment_id,runnable,db):
    try:
        with open("app/trainWorker/model.py", "rt") as file:
            reads = file.read()

        with open("app/trainWorker/model.py", "wt") as file:
            reads = reads.replace("### LAYER DATA ###", runnable)
            file.write(reads)

        logger.info(f"reads: {reads}")
        await containerCRUD.updatePythonSources(db=db, experiment_id=experiment_id,runnable=reads)
    except:
        logger.error(f"Errors in injectLayer.")
        traceback.print_exc()
        # Spring에서 HttpStatus 로 판단해서 Update.
        # await containerCRUD.updateStatus(db=db, expriment_id=experiment_id, status="Failed")
    file.close()
