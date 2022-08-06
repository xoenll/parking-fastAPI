from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class Car(Model):

    class Meta:
        table_name = 'oop_car'
        host = "http://localhost:8000"

    license_plate = UnicodeAttribute(hash_key=True)
    color = UnicodeAttribute()
    size = UnicodeAttribute()
