class AlreadyExists(Exception):
    def __init__(self, short_url: str, code: int):
        self.msg = f"entity with short url {short_url} already exists"
        self.code = code
