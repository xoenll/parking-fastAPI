
from typing import List
from pydantic import BaseModel


class EntryPointSchema(BaseModel):
    entry_id: str
    status: int


class MultiEntryPointSchema(BaseModel):
    entry_points: List[EntryPointSchema]


class ParkingSlotSchema(BaseModel):
    slot_id: str
    size: str
    status: int
    distance_map: str


class ParkingMapSchema(BaseModel):
    parking_slots: List[ParkingSlotSchema]


class ParkingEntrySchema(BaseModel):
    entry_id: str
    plate_id: str
    size: str
    time: str
