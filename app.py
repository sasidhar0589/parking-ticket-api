from flask import Flask, request
from markupsafe import escape
import json
from flask_smorest import Api
from blueprint.parking_locations_blueprint import parking_locations_blueprint

app = Flask(__name__)
app.config["API_TITLE"] = "Parking ticket REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)
api.register_blueprint(parking_locations_blueprint)

# @app.route('/parking_information')
# def parking_information():
#     return 'available parking spots'

# @app.route('/parking_prices/<int:parking_id>')
# def parking_prices():
#     return 'parking prices'

# @app.route('/parkinghistory/<int:parking_id>')
# def parking_history(parking_id):
#     return f'Parking history for parking id {parking_id}'
# @app.get('/parkinglocations/')
# def parking_locations():
#     result = get_parking_location()
#     print(result)
#     return result
# @app.get('/parkinglocations/<int:parking_id>')
# def parking_location_by_id(parking_id):
#     result = get_parking_location_by_id(parking_id)
#     print(result)
#     return result
    
# @app.post('/parkinglocations/')
# def add_parking_location():
#     request_data = request.get_json()
#     print(request_data)
#     result = insert_parking_location(request_data)
#     return result
# @app.patch('/parkinglocations/')
# def update_parking_location():
#     request_data = request.get_json()
#     print(request_data)
#     result = update_parking_location_table(data=request_data)
#     return result
# @app.delete('/parkinglocations/<int:parking_id>')
# def delete_parking_location(parking_id):
#     result = delete_parking_location_record(parking_id)
#     return result

# @app.route('/about')
# def about():
#     return 'Parking ticket API'
