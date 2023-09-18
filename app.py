from typing import Union

import uvicorn
from fastapi import FastAPI

from db_start_up_config import mysql_db
from helpers.hash_generator import HashGenerator
from managers.shorter_url_service_manager import ShorterUrlServiceManager
from proto.protoEntities import GenerateShorterUrlRequest

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    mysql_db.connect()


@app.on_event("shutdown")
async def shutdown_db_client():
    mysql_db.disconnect()


db = mysql_db
hash_generator = HashGenerator()
service_manager = ShorterUrlServiceManager(hash_generator, db)


@app.get("/get_origin_url")
async def get_origin_url(url: Union[str, None]):
    if url is not None:
        origin_url = await service_manager.get_origin_url(url)
        return origin_url


@app.post("/generate_shorter_short")
async def generate_shorter_url(generate_shorter_url_request: GenerateShorterUrlRequest):
    url_mapping_domain = await service_manager.generate_shorter_url(generate_shorter_url_request.url)
    return url_mapping_domain

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
