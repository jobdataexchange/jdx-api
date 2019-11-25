from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from jdxapi.utils.functions import RequestHandler, ResponseHandler
from jdxapi.app import api, DB
from jdxapi.models import Pipeline, FrameworkRecommendation
from jdxapi.services.competensor import get_framework_recommendations
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import jdxapi.utils.constants as c
import datetime


@api.resource("/get-score")
class GetScore(LoggerResource):
    
    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        _ = Pipeline.get_pipeline_from_id(pipeline_id)

        score, explanation = Pipeline.calculate_score(pipeline_id)

        resp = {
            c.PIPELINE_ID: str(pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now()),
            "score": str(score),
            "explanation": str(explanation)
        }

        response = ResponseHandler.create_response(resp, 200)
        return response
