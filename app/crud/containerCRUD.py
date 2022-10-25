import logging

from sqlalchemy.orm import Session

from app.entity.containerEntity import Container

logger = logging.getLogger('trainer')

def getContainerByExperimentId(db: Session, experiment_id: bytes):
    logger.info(f"experiment_id: f{experiment_id}")
    return db.query(Container).filter(Container.experiment_id == experiment_id).first()
