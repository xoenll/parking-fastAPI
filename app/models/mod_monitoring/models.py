from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute
from datetime import datetime
import uuid


class ParkingTransaction(Model):

    class Meta:
        table_name = "oop_parking_transaction"
        host = "http://localhost:8000"

    transaction_id = UnicodeAttribute(
        hash_key=True, default=lambda: str(uuid.uuid1())[:8].upper())
    transaction_datetime = UTCDateTimeAttribute(range_key=True)
    type = NumberAttribute()


class ParkingHistory(Model):
    class Meta:
        table_name = "oop_parking_history"

    parking_history_id_format = "{plate}#{timestamp}"
    parking_history_id = UnicodeAttribute(hash_key=True)
    date_time_start = UTCDateTimeAttribute()
    date_time_end = UTCDateTimeAttribute(null=True)
    slot_id = UnicodeAttribute()
    plate_id = UnicodeAttribute()
    ancestor_transaction = UnicodeAttribute(null=True)
    exit_transaction = UnicodeAttribute(null=True)
    size = UnicodeAttribute()
    rate = NumberAttribute()
    total_fee = NumberAttribute(null=True)
