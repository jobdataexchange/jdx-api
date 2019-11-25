from jdxapi.app import api, DB
from jdxapi.models import Pipeline
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from jdxapi.utils.logger_resource import LoggerResource
from flask import request
import datetime
from jdxapi.utils.functions import RequestHandler, ResponseHandler
import jdxapi.utils.constants as c

@api.resource('/user-actions')
class UserActions(LoggerResource):

    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        pipeline = Pipeline.get_pipeline_from_id(pipeline_id)

        match_table_selections = RequestHandler.get_match_table_selections(
            req,
            True
        )
        
        self.set_match_table_selections(pipeline, match_table_selections)
        
        response_data = self.make_response_data(pipeline_id, pipeline, match_table_selections)
        response = ResponseHandler.create_response(response_data, 200)
        return response
    
    
    def set_match_table_selections(self, pipeline, match_table_selections):
        pipeline.match_table_selections = match_table_selections
        DB.session.commit()


    def make_response_data(self, pipeline_id, pipeline, match_table_selections):
        response_data = {
            c.PIPELINE_ID: str(pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now())
        }
        return response_data
