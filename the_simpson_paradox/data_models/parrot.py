from enum import Enum


class Parrot(str, Enum):
    you: str = "You"
    polly: str = "Polly"
    peter: str = "Peter"