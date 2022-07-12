from enum import Enum


class RegEx(Enum):
    NAME = (
        r'^[\w.]{2,50}$',
        'letters, numbers and symbols ("_", ".") between 2 and 50 characters'
    )

    def __init__(self, pattern: str, msg: str):
        self.pattern = pattern
        self.msg = msg
        

