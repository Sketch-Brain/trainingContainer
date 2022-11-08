from logging.config import dictConfig

from fastapi import FastAPI, Depends


from app.api import trainerController
from app.logging_config import logging_config
from app.db.database import engine
from app.dependencies import get_query_token
from app.entity import containerEntity

containerEntity.Base.metadata.create_all(bind=engine)
dictConfig(logging_config)
app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(trainerController.trainerRouter)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=False,
        port=8888
    )
