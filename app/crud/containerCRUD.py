import logging

from sqlalchemy.orm import Session

from app.entity.containerEntity import Container

logger = logging.getLogger('trainer')


async def getContainerByExperimentId(db: Session, experiment_id: bytes):
    logger.info(f"experiment_id: f{experiment_id}")
    return db.query(Container).filter(Container.experiment_id == experiment_id).first()


async def updatePythonSources(db: Session, experiment_id: bytes, runnable: str):
    logger.info("Update python_sources by created.")
    logger.debug(f"experiment_id : {experiment_id}")

    workers = db.query(Container).first()
    logger.debug(f"workers : {workers.experiment_id},{workers.python_source}")

    worker = db.query(Container).filter(Container.experiment_id == experiment_id).first()
    worker.python_source = runnable
    db.commit()


async def updateStatus(db: Session, expriment_id: bytes, status: str):
    logger.info(f"Update experiment Status to {status}")
    db.query(Container).filter(Container.experiment_id == expriment_id).updatye({'status': status})
    db.commit()
