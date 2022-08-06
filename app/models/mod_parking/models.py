from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class EntryPoint(Model):
    class Meta:
        table_name = "oop_entry_point"
        host = "http://localhost:8000"

    entry_id = UnicodeAttribute(hash_key=True)
    status = NumberAttribute(range_key=True)


class ParkingSlot(Model):
    class Meta:
        table_name = "oop_parking_slot"
        host = "http://localhost:8000"

    slot_id = UnicodeAttribute(hash_key=True)
    size = UnicodeAttribute(range_key=True)
    status = NumberAttribute()
