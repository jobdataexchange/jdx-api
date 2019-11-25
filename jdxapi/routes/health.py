from jdxapi.app import api
from flask_restful import Resource
from flask import request, jsonify
from jdxapi.services.competensor import health


@api.resource('/health')
class Health(Resource):
    def get(self):
        resp_data = {'api': 200}
        response = jsonify(resp_data)
        response.status_code = 200
        return response


@api.resource('/health-competensor')
class HealthCompetensor(Resource):
    def get(self):
        act_status = health()
        resp_data = {'api': 200, 'competensor': act_status}
        response = jsonify(resp_data)
        response.status_code = 200
        return response
