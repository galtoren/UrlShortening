from typing import Union

import uvicorn
from fastapi import FastAPI

from db_start_up_config import mysql_db
from proto.protoEntities import GenerateShorterUrlRequest

app = FastAPI()



@app.on_event("startup")
async def startup_db_client():
    mysql_db.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    mysql_db.disconnect()

@app.get("/get_shorter_url")
async def get_shorter_url(url: Union[str, None]):
    if url is not None:
        return

@app.post("/generate_shorter_short")
async def generate_shorter_url(generate_shorter_url_request: GenerateShorterUrlRequest):
    return



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
