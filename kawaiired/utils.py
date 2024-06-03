from dataclasses import dataclass


BASE_URL = "https://kawaii.red/api"


@dataclass
class Stats:
    endpoints: list
    all: int
    failed: int
    history: list
    most_endpoint: dict
    most_endpoints: list
    most_type: dict
    most_types: list
