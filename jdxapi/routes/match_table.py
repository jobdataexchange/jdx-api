from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from jdxapi.app import api, DB
from jdxapi.models import Pipeline
from jdxapi.utils.functions import RequestHandler, ResponseHandler
from jdxapi.services.competensor import get_match_table
import datetime


@api.resource('/match-table')
class MatchTable(LoggerResource):
    
    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        threshold = RequestHandler.get_threshold(req, False)
        frameworks = Pipeline.get_frameworks_from_pipeline_id(pipeline_id)

        match_table_data = get_match_table(pipeline_id, frameworks, threshold)
        response = ResponseHandler.create_response(match_table_data, 200)
        return response
