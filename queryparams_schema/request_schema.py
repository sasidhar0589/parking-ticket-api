from marshmallow import Schema, fields

class RequestSchema(Schema):
    """Schema for request body."""
        # "id":4,
        #     "parking_locationname": "AUSTIN-downtown",
        #     "parking_locationtype": "airport-cell-lot",
        #     "parking_locationaddress": "Austin texas",
        #     "parking_id": 4
    # Define the fields for the request body
    id = fields.Int(required=True, description="Description for param1")
    parking_locationname = fields.Str(required=False, description="Description for param2")
    parking_locationtype = fields.Str(required=False, description="Description for param3")
    parking_locationaddress = fields.Str(required=False, description="Description for param4")
    parking_id = fields.Int(required=True, description="Description for param5")