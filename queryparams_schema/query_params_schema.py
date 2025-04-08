from marshmallow import Schema, fields
class QueryParamsSchema(Schema):
    """Schema for query parameters."""

    # Define the fields for the query parameters
    parking_location_id = fields.Int(required=False, description="Description for param1")