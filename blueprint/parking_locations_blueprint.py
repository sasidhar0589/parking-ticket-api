from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from queryparams_schema.query_params_schema import QueryParamsSchema
from queryparams_schema.request_schema import RequestSchema
from data.db import (
    get_parking_location,
    get_parking_location_by_id,
    insert_parking_location,
    update_parking_location_table,
    delete_parking_location_record
)
parking_locations_blueprint = Blueprint(
    'parking_locations',
    __name__,
    description='Operations on parking locations'
)
@parking_locations_blueprint.route('/parkinglocations/')
class ParkingLocationsAPI(MethodView):
    @parking_locations_blueprint.arguments(QueryParamsSchema, location='query')
    def get(self, args):
        if args.get('parking_location_id') is None:
            result = get_parking_location()
            return result
        else:
            print(args.get('parking_location_id'))
            result = get_parking_location_by_id(args.get('parking_location_id'))
            print(result)
            if not result:
                abort(404, message=f"Parking location {args.get('parking_location_id')} not found")
            return result

    def post(self):
        request_data = request.get_json()
        request_data = RequestSchema().load(request_data)
        if not request_data:
            abort(400, message="Invalid request data")
        result = insert_parking_location(request_data)
        if not result:
                abort(500, message="Parking location insert failed")
        return result

    def patch(self):
        request_data = request.get_json()
        result = update_parking_location_table(data=request_data)
        if not result:
                abort(500, message="Parking location update failed")
        return result

    def delete(self, parking_id):
        result = delete_parking_location_record(parking_id)
        if not result:
            abort(500, message="Parking location update failed")
        return result