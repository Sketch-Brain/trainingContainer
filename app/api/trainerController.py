import asyncio
import logging
import os

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies import get_token_header
from app.crud import containerCRUD
from app.api.trainerService import injectLayer
from app.trainWorker import runs
from bson import ObjectId


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
    container = await containerCRUD.getContainerByExperimentId(db=db, experiment_id=experimentId)
    return container


@trainerRouter.post("/insertRunnable")
async def insertRunnable(
        payload: dict = Body(...)
        , db: Session = Depends(get_db)
):
    # 이 Bytes는 이미 database 형식과 모두 일치하는 형태로 experiment_id 가 온다.
    # experiment_id = payload['experimentId']
    experiment_id = ObjectId(payload['experimentId']).binary # Experiment Id 값으로 추출.
    runnable = payload['runnable'][:-2]  # Last char ',\n' delete.
    logger.info(f"Insert Runnable : {runnable}")
    await injectLayer(experiment_id=experiment_id, runnable=runnable, db=db)
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
    strExpId = payload['experimentId']
    experiment_id = ObjectId(payload['experimentId']).binary #Experiment_id 추가.
    userId = os.environ.get("userId")
    # Background training Runs.
    # FIXME model Load 하는 함수는, Background 작동하기 이전에 여기서 검사해야 함. 그래야, Request 돌려주기 전에 에러 검사 가능.
    asyncio.create_task(runs.runMnistExperiment(db=db, userId=userId, experiment_id=experiment_id, strExpId=strExpId))
    return {"run": "success"}
