from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
import uuid


class ParkingTransaction(Model):

    class Meta:
        table_name = "oop_parking_transaction"
        host = "http://localhost:8000"

    transaction_id = UnicodeAttribute(
        hash_key=True, default=lambda: str(uuid.uuid1())[:8].upper())
    transaction_datetime = UTCDateTimeAttribute(range_key=True)
    type = NumberAttribute()
