from jdxapi.app import api, DB
from jdxapi.models import Pipeline, FrameworkRecommendation, Framework
from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from jdxapi.utils.error import ApiError
from jdxapi.utils.functions import RequestHandler
import datetime
import jdxapi.utils.constants as c
from jdxapi.utils.functions import RequestHandler, ResponseHandler


@api.resource("/framework-selections")
class FrameworkSelections(LoggerResource):

    def post(self):
        req = request.get_json()

        pipeline_id = RequestHandler.get_pipeline_id(req, True)        
        pipeline = Pipeline.get_pipeline_from_id(pipeline_id)
        
        competencies = req[c.FRAMEWORKS].get(c.COMPETENCY)
        occupations = req[c.FRAMEWORKS].get(c.OCCUPATION)
        industries = req[c.FRAMEWORKS].get(c.INDUSTRY)
        
        self.validate(pipeline_id, competencies)

        frameworks = self.compile_frameworks(competencies, occupations, industries)
        self.store_given_frameworks(pipeline, frameworks)

        resp_data = self.create_response_data(pipeline_id)
        response = ResponseHandler.create_response(resp_data, 200)
        return response


    def validate(self, pipeline_id, competencies):
        if not pipeline_id:
            raise ApiError(f"Must have a '{c.PIPELINE_ID}''", 422)

        if not competencies:
            raise ApiError("Must have at least one competency", 422)


    def compile_frameworks(self, *framework_lists):
        frameworks = []
        for framework in framework_lists:
            if framework:
                frameworks += [*framework]

        return frameworks


    def store_given_frameworks(self, pipeline, frameworks):
        # Pass frameworks to pipeline
        given_frameworks = [item[c.FRAMEWORK_ID] for item in frameworks]
        
        for framework_id in given_frameworks:
            that_framework = Framework.get_framework_from_id(framework_id)
            pipeline.frameworks.append(that_framework)

        DB.session.commit()

    def create_response_data(self, pipeline_id):
        resp_data = {
            c.PIPELINE_ID: str(pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now()),
        }

        return resp_data
