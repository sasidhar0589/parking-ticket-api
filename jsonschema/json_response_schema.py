import json 

def generate_json_response_schema(model):
    schema = {  
        "type": "object",
        "properties": {},
    }
    for column in model.__table__.columns:
        column_type = "string"
        if column.type.__class__.__name__ == 'Integer':
            column_type = "integer"
        elif column.type.__class__.__name__ == 'String':
            column_type = "string"
        elif column.type.__class__.__name__ == 'Float':
            column_type = "number"
        elif column.type.__class__.__name__ == 'Boolean':
            column_type = "boolean"
        schema["properties"][column.name] = {
            "type": column_type
        }
        if column.primary_key:
            schema["properties"][column.name]["primary_key"] = True
    return json.dumps(schema, indent=4)