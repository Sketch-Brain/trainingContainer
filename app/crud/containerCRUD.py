from sqlalchemy.orm import Session

from app.entity import containerEntity


def getContainerByExperimentId(db: Session, experiment_id: bytes):
    return db.query(containerEntity).filter(containerEntity.experiment_id == experiment_id).first()
