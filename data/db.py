import sqlalchemy
# from jsonschema.jsonschema import  generate_json_schema
# from jsonschema.json_response_schema import generate_json_response_schema
from sqlalchemy.orm import  DeclarativeBase
import json
class Base(DeclarativeBase):
    pass
from sqlalchemy import create_engine, text, Column, Integer, String, Select, select, insert
engine = create_engine('mysql://<user>:<pass>@localhost/parkinglot', echo=True)
connection = engine.connect()



class ParkingTable(Base):
    __tablename__ = 'parking_table'
    __type__ = 'ParkingInformation'
    id = Column(Integer, primary_key=True)
    parking_location_id = Column(Integer)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    parking_time_id = Column(String)
    parking_ammount = Column(String)
    parking_account_id = Column(Integer)
    

class ParkingLocation(Base):
    __tablename__ = 'parking_location'
    __type__ = 'ParkinglocationInformation'
    id = Column(Integer, primary_key=True)
    parking_locationname = Column(String)
    parking_locationtype = Column(String)
    parking_locationaddress = Column(String)
    parking_id = Column(Integer)

def get_parking_ticket_by_id(number):
    stmt = select(ParkingTable).where(ParkingTable.id == number)
    result = connection.execute(stmt)
    return result.fetchall()
def get_praking_price(number):
    stmt = select(ParkingTable.parking_ammount).where(ParkingTable.id == number)
    result = connection.execute(stmt)
    return result.fetchall()
def get_parking_location():
     stmt = select(ParkingLocation)
     result = connection.execute(stmt)
     return generate_json_response(ParkingLocation, result)     
def get_parking_location_by_id(number):
    stmt = select(ParkingLocation).where(ParkingLocation.id == number)
    result = connection.execute(stmt)
    result = generate_json_response(ParkingLocation, result)
    return result
def insert_parking_location(data):
    
    stmt = insert(ParkingLocation).values(id = data['id'],parking_locationname=data['parking_locationname'], parking_locationtype=data['parking_locationtype'], parking_locationaddress=data['parking_locationaddress'], parking_id=data['parking_id'])
    connection.execute(stmt)
    connection.commit()
    return get_parking_location()
def generate_json_response(model, result):
    response = []
    for row in result:
        response.append({column.name: getattr(row, column.name) for column in model.__table__.columns})
    return json.dumps(response, indent=4)