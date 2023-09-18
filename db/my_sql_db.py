from typing import Union

from db.db_interface import DataBaseInterface


class MySqlDB(DataBaseInterface):

    async def get_shorter_url(self, url: str) -> Union[str, None]:
        pass

    async def generate_shorter_url(self, url: str) -> Union[str, None]:
        pass