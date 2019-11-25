from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from jdxapi.utils.functions import RequestHandler, ResponseHandler
from jdxapi.app import api, DB
from jdxapi.models import Pipeline, FrameworkRecommendation
from jdxapi.services.competensor import get_framework_recommendations
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime


@api.resource("/framework-recommendations")
class FrameworkRecommendations(LoggerResource):
    
    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        _ = Pipeline.get_pipeline_from_id(pipeline_id)

        framework_recommendations = get_framework_recommendations(pipeline_id)

        response = ResponseHandler.create_response(framework_recommendations, 200)
        return response
