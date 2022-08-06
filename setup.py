from asyncore import write
from app.models.mod_car.models import Car
from app.models.mod_monitoring.models import ParkingTransaction
from app.models.mod_parking.models import ParkingSlot, EntryPoint
import os

os.environ["PYNAMODB_CONFIG"] = "{}/{}".format(os.getcwd(), "setup.py")

Car.create_table(read_capacity_units=1, write_capacity_units=1)
ParkingTransaction.create_table(read_capacity_units=1, write_capacity_units=1)
ParkingSlot.create_table(read_capacity_units=1, write_capacity_units=1)
EntryPoint.create_table(read_capacity_units=1, write_capacity_units=1)
