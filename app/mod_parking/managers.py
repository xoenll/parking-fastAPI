from datetime import datetime
import json
from app.models.mod_monitoring.models import ParkingTransaction, ParkingHistory
from app.models.mod_monitoring.statics import TransactionType, ParkingRates
from app.models.mod_parking.models import ParkingSlot
from app.models.mod_parking.statics import SlotStatus, SlotSize
from app.models.mod_car.statics import CarSize


class ParkingManager:
    def handle_entry(entry_id: str, plate_id: str, size: str, time: str) -> ParkingHistory:
        hour, minutes = time.split(":")
        rate = ParkingRates[size]
        date_now = datetime.utcnow()
        current_datetime = datetime(
            date_now.month(), date_now.day(), date_now.year(), hour, minutes, 0)
        parking_transaction = ParkingTransaction(
            transaction_datetime=current_datetime,
            type=TransactionType.ENTRY
        )
        parking_transaction.save()
        slot = retrieve_parking_slot(entry_id=entry_id, size=size)
        parking_history_entry = ParkingHistory(
            parking_history_id=ParkingHistory.parking_history_id_format.format(
                plate=plate_id, timestamp=current_datetime.timestamp()),
            date_time_start=current_datetime,
            plate_id=plate_id,
            size=size,
            rate=rate,
            slot_id=slot
        )
        parking_history_entry.save()

        occupied_slot = ParkingSlot.get(slot)
        occupied_slot.status = SlotStatus.OCCUPIED
        occupied_slot.save()

    @staticmethod
    def retrieve_parking_slot(entry_id: str, size: str) -> str:
        size_map = {
            CarSize.SMALL: [SlotSize.SMALL, SlotSize.MEDIUM, SlotSize.LARGE],
            CarSize.MEDIUM: [SlotSize.MEDIUM, SlotSize.LARGE],
            CarSize.LARGE: [SlotSize.LARGE]
        }

        applicable_slot_sizes = size_map[size]
        entry_distance = 0
        slot_id = None
        for slot in ParkingSlot.scan((ParkingSlot.status == SlotStatus.FREE) & ParkingSlot.size in applicable_slot_sizes):
            slot_distance_map = json.loads(slot.distance_map)
            slot_distance = slot_distance_map[entry_id]
            if entry_distance == 0:
                entry_distance = slot_distance
            elif entry_distance > slot_distance:
                entry_distance = slot_distance
                slot_id = slot.slot_id

        return slot_id
