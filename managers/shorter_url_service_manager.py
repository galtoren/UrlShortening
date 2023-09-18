from db.domain_entities import UrlDomainEntity
from db.my_sql_db import MySqlDB
from helpers.hash_generator import HashGenerator


class ShorterUrlServiceManager:
    def __init__(self, hash_generator: HashGenerator, mysql_db: MySqlDB):
        self._hash_generator = hash_generator
        self._db = mysql_db

    async def get_origin_url(self, short_url: str):
        url_mapping_domain = await self._db.get_origin_url(short_url)
        return url_mapping_domain.origin_url

    async def generate_shorter_url(self, long_url: str):
        hashed_url = self._hash_generator.generate_hash(long_url)
        url_mapping_domain = UrlDomainEntity(origin_url=long_url, shorter_url=hashed_url)
        created_url_mapping_domain = await self._db.generate_shorter_url(url_mapping_domain)
        return created_url_mapping_domain
