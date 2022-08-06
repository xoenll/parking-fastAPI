from pydantic import BaseModel


class CarSchema(BaseModel):
    license_plate: str
    color: str
    size: str
