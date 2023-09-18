from abc import abstractmethod
from typing import Union


class DataBaseInterface:
    @abstractmethod
    async def get_shorter_url(self, url: str) -> Union[str, None]:
        pass

    @abstractmethod
    async def generate_shorter_url(self, url: str) -> Union[str, None]:
        pass
