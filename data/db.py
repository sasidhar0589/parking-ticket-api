import sqlalchemy

# from jsonschema.jsonschema import  generate_json_schema
# from jsonschema.json_response_schema import generate_json_response_schema
from sqlalchemy.orm import  DeclarativeBase,scoped_session,sessionmaker
import json
class Base(DeclarativeBase):
    pass
from sqlalchemy import create_engine, text, Column, Integer, String, Select, select, insert, update
DATABASE_URI = "mysql://<usr>:<pass>@localhost/parkinglot"
engine = create_engine(DATABASE_URI, echo=True)
sessiondb = scoped_session(sessionmaker(autoflush= True, bind=engine))

def get_db():
    db = sessiondb()
    try:
        yield db
    finally:
        db.close()


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

# def get_parking_ticket_by_id(number):
#     stmt = select(ParkingTable).where(ParkingTable.id == number)
#     result = connection.execute(stmt)
#     return result.fetchall()
# def get_praking_price(number):
#     stmt = select(ParkingTable.parking_ammount).where(ParkingTable.id == number)
#     result = connection.execute(stmt)
#     return result.fetchall()
def get_parking_location():
    db = next(get_db())
    result = db.query(ParkingLocation).all()
    return result
def get_parking_location_by_id(number):
    db = next(get_db())
    result = db.query(ParkingLocation).where(ParkingLocation.id == number).all()
    return result
def insert_parking_location(data): 
    db = next(get_db())
    new_parking_location = ParkingLocation(**data)
    db.add(new_parking_location)
    db.flush()
    db.commit()
    return get_parking_location()
def update_parking_location_table(data):
    db = next(get_db())
    db.query(ParkingLocation).filter(ParkingLocation.id == data['id']).update({
        ParkingLocation.parking_locationname: data['parking_locationname'],
        ParkingLocation.parking_locationtype: data['parking_locationtype'],
        ParkingLocation.parking_locationaddress: data['parking_locationaddress'],
        ParkingLocation.parking_id: data['parking_id']
    })
    db.commit()
    return get_parking_location()
def delete_parking_location_record(number):
    db = next(get_db())
    db.query(ParkingLocation).filter(ParkingLocation.id == number).delete()
    db.commit()
    return get_parking_location()