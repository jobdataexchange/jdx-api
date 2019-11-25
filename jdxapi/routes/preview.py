from flask import request, jsonify
from jdxapi.utils.logger_resource import LoggerResource
from jdxapi.app import api, DB
from jdxapi.models import Pipeline
from jdxapi.utils.functions import RequestHandler, ResponseHandler
from jdxapi.utils.error import ApiError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import jdxapi.utils.constants as c
from jdxapi.services.competensor import get_preview


@api.resource("/preview")
class Preview(LoggerResource):

    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        _ = Pipeline.get_pipeline_from_id(pipeline_id)

        preview_data = get_preview(pipeline_id)
        resp_data = self.create_response_data(pipeline_id, preview_data, req)
        response = ResponseHandler.create_response(resp_data, 200)
        return response


    def create_response_data(self, pipeline_id, preview_data, req):
        resp_data = {
            c.PIPELINE_ID: str(pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now()),
            "preview": preview_data
        }

        return resp_data
