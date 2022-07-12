from enum import Enum


class RegEx(Enum):
    BRAND = (
        r'^([\w-]{2,50})$',
        'letters, numbers and symbols ("_", "-") between 2 and 50 characters'
    )
    PRICE = (
        r'^(200\d|20[1-9]\d|2[1-9]\d{2}|[3-9]\d{3}|[1-9]\d{4}|100000)$',
        'number between 2000 and 100000'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
        

