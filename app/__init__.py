from fastapi import FastAPI
from app.schemas.mod_parking.schemas import EntryPointSchema, MultiEntryPointSchema, ParkingMapSchema
from app.models.mod_parking.models import EntryPoint, ParkingSlot

app = FastAPI()


@app.post("/entry-point/")
async def create_entry_point(entry_point: EntryPointSchema):
    new_entry_point = EntryPoint(
        entry_id=entry_point.entry_id, status=entry_point.status)
    new_entry_point.save()


@app.post("/entry-points/")
async def create_entry_points(entry_points: MultiEntryPointSchema):
    for entry_point in entry_points.entry_points:
        new_entry_point = EntryPoint(
            entry_id=entry_point.entry_id, status=entry_point.status)
        new_entry_point.save()


@app.post("/parking-map/")
async def set_parking_map(parking_map: ParkingMapSchema):
    for parking_slot in parking_map.parking_slots:
        print(parking_slot)
        query = ParkingSlot.query(hash_key=parking_slot.slot_id)
        items = list(query)
        query_result = items[0] if len(items) > 0 else None
        if(query_result):
            # Add response for each slot that already exists
            continue
        print("parking does not exist yet")
        new_parking_slot = ParkingSlot(slot_id=parking_slot.slot_id, size=parking_slot.size,
                                       status=parking_slot.status, distance_map=parking_slot.distance_map)

        new_parking_slot.save()
