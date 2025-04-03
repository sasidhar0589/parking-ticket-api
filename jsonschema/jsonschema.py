
import json
def generate_json_schema(model):
    schema= {  
             "type": "object",
                "properties": {},
            }
    for column in model.__table__.columns:
        column_type = "string"
        schema["properties"][column.name] = {
            "type": column_type
        }
        if column.primary_key:
            schema["properties"][column.name]["primary_key"] = True
    return json.dumps(schema, indent=4)