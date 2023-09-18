from dataclasses import dataclass


@dataclass
class UrlDomainEntity:
    origin_url: str
    shorter_url: str
