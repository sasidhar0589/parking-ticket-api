from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from data.db import ParkingLocation
class ParkingLocationResponseSchema(SQLAlchemyAutoSchema):
    """Schema for parking location response."""
    class Meta:
        model = ParkingLocation
        load_instance = True
        include_fk = True
        # exclude = ('id',)