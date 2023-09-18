from dataclasses import dataclass


@dataclass
class GenerateShorterUrlRequest:
    url: str
