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