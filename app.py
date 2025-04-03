from flask import Flask, request
from markupsafe import escape
import json
from data.db import (
    get_parking_ticket_by_id, 
    get_praking_price, 
    get_parking_location, 
    get_parking_location_by_id,
    insert_parking_location)

app = Flask(__name__)

@app.route('/parking_information')
def parking_information():
    return 'available parking spots'

@app.route('/parking_prices/<int:parking_id>')
def parking_prices():
    return 'parking prices'

@app.route('/parkinghistory/<int:parking_id>')
def parking_history(parking_id):
    return f'Parking history for parking id {parking_id}'
@app.get('/parkinglocations/')
def parking_locations():
    result = get_parking_location()
    print(result)
    return result
@app.get('/parkinglocations/<int:parking_id>')
def parking_location_by_id(parking_id):
    result = get_parking_location_by_id(parking_id)
    print(result)
    return result
    
@app.post('/parkinglocations/')
def add_parking_location():
    request_data = request.get_json()
    print(request_data)
    result = insert_parking_location(request_data)
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print(result)
    return result
     
     

@app.route('/about')
def about():
    return 'Parking ticket API'
