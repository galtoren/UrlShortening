from typing import Union

from sqlalchemy import select

from db.db_interface import DataBaseInterface
from db.domain_entities import UrlDomainEntity
from db_start_up_config import mysql_db, url_mappings


class MySqlDB(DataBaseInterface):

    async def get_origin_url(self, hashed_url: str) -> UrlDomainEntity:
        query = select([url_mappings]).where(url_mappings.c.shorter_url == hashed_url)
        result = mysql_db.execute(query)

        # Fetch one row - assume there is only on with the same id (PrimaryKey)
        url_data = result.fetchone()
        if url_data:
            url_mappings_domain = UrlDomainEntity(origin_url=url_data['origin_url'], shorter_url=url_data['shorter_url'])
            return url_mappings_domain

    async def generate_shorter_url(self, url_domain_entity: UrlDomainEntity) -> UrlDomainEntity:
        pass
