from dataclasses import dataclass


@dataclass
class Message:
    id: int = 0
    user: str = ''
    text: str = ''
    like: int = 0
