from typing import Union

import uvicorn
from fastapi import FastAPI

from db.my_sql_db import MySqlDB
from db_start_up_config import mysql_db
from exceptions.already_exists_exception import AlreadyExists
from exceptions.not_found_exception import NotFound
from helpers.error_generator import ErrorsGenerator
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


error_generator = ErrorsGenerator()
db = MySqlDB()
hash_generator = HashGenerator()
service_manager = ShorterUrlServiceManager(hash_generator, db)


@app.get("/get_origin_url")
async def get_origin_url(url: Union[str, None]):
    if url is not None:
        try:
            origin_url = await service_manager.get_origin_url(url)
            return origin_url
        except NotFound as e:
            return error_generator.generate_error(e.code, e.msg)
        except Exception as e:
            return error_generator.generate_error(500, f"InternalError: unexpected error: {e}")
    else:
        return error_generator.generate_error(400, "Invalid Argument: url param can't be empty")


@app.post("/generate_shorter_url")
async def generate_shorter_url(generate_shorter_url_request: GenerateShorterUrlRequest):
    try:
        url_mapping_domain = await service_manager.generate_shorter_url(generate_shorter_url_request.url)
        return url_mapping_domain
    except AlreadyExists as e:
        return error_generator.generate_error(409,
                                              f"AlreadyExists: shorter url for: {generate_shorter_url_request.url} is "
                                              f"already exists")
    except Exception as e:
        return error_generator.generate_error(500, f"InternalError: unexpected error: {e}")


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
