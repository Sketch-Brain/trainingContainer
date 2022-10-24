from fastapi import FastAPI, Depends


from api import trainerController
from db.database import engine
from dependencies import get_query_token
from entity import containerEntity

containerEntity.Base.metadata.create_all(bind=engine)
app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(trainerController.trainerRouter)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8888
    )
