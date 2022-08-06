from pydantic import BaseModel
from datetime import datetime


class ParkingTransactionSchema(BaseModel):
    transaction_id: str
    transaction_datetime: datetime
    type: int
