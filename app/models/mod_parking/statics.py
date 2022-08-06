from enum import Enum


class EntryStatus:
    CLOSED = 0
    OPEN = 1


class SlotStatus:
    FREE = 0
    OCCUPIED = 1
    RESERVED = 2


class SlotSize(Enum):
    SMALL = "SP"
    MEDIUM = "MP"
    LARGE = "LP"
