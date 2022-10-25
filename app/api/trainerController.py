import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.dependencies import get_token_header
from app.crud import containerCRUD


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


logger = logging.getLogger("trainer")

trainerRouter = APIRouter(
    prefix="/trainer/container",
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
        runnable: str
):
    print("runnable")
