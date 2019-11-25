import uuid
import os
import sys
from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_key
# import jdxapi.routes.upload_job_description as utils

# from model_setup import setup_environment, restore_environment, get_app, get_db
from ...pocha_setup import application, DB

from jdxapi.models import FrameworkRecommendation, Pipeline, Framework, FrameworkType
import datetime

match_table_selections = [
    {
        "substatementID": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
        "substatement": "Can perform test driven development",
        "selection": {
            "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "what is this for?",
            "descrtiption": "Performs TDD",
            "definedTermSet": "Standard Occupational Classification system",
            "termCode": "19-1131.00",
            "value": "0.9"
        }
    }
]

@describe('/user-acitons')
def _():
    
    @it('can post selections to pipeline')
    def _():

        my_pipeline = Pipeline()

        DB.session.add(my_pipeline)

        DB.session.commit()

        my_pipeline_id = my_pipeline.pipeline_id

        request_body = {
            "pipelineID": str(my_pipeline_id),
            "matchTableSelections": match_table_selections
        }

        expected_response = {
            # "timestamp": "",
            "pipelineID": str(my_pipeline_id)
        }

        resp = application.post_json('/user-actions', request_body)

        expect(resp.status_int).to(equal(200))

        expect(my_pipeline.match_table_selections).to(equal(match_table_selections))
        # expect(resp.json).to(equal(expected_response))

        # @it('rejects bad data')
        # def _():
        #     pass
