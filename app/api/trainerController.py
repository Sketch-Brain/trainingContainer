import logging
import os

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies import get_token_header
from app.crud import containerCRUD
from app.api.trainerService import injectLayer
from app.trainWorker import runs


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logger = logging.getLogger("trainer")

trainerRouter = APIRouter(
    prefix="/trainer/worker",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@trainerRouter.get("/getStatus")
async def getTrainingStatus():
    return {"message": "Hello World"}


@trainerRouter.get("/getContainer/{experimentId}")
async def getContainerData(
        experimentId: bytes
        , db: Session = Depends(get_db)
):
    logger.info(f"Id : {experimentId}")
    container = containerCRUD.getContainerByExperimentId(db=db, experiment_id=experimentId)
    return container


@trainerRouter.post("/insertRunnable")
async def insertRunnable(
        payload: dict = Body(...)
        , db: Session = Depends(get_db)
):
    runnable = payload['runnable'][:-2]  # Last char ',\n' delete.
    logger.info(f"Insert Runnable : {runnable}")
    await injectLayer(runnable=runnable)
    return {"success": True}


@trainerRouter.get("/health")
async def isReady():
    return {"status":200}


@trainerRouter.patch("/run")
async def runWorker(
        payload: dict = Body(...),
        db: Session = Depends(get_db)
):
    logger.info("Training run started.")
    userId = os.environ.get("USER_ID")
    # THIS IS TEST.
    runs.runMnistExperiment()
    return {"run": "success"}
