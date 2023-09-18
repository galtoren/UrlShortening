from abc import abstractmethod
from typing import Union

from db.domain_entities import UrlDomainEntity


class DataBaseInterface:
    @abstractmethod
    async def get_origin_url(self, url: str) -> UrlDomainEntity:
        pass

    @abstractmethod
    async def generate_shorter_url(self, url_domina_entity: UrlDomainEntity) -> UrlDomainEntity:
        pass
