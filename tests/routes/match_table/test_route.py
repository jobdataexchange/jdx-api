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

match_table_dict = {
    "matchTable": [
        {
            "substatementID": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
            "substatement": "Can perform test driven development",
            "matches": [
                {
                    "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "what is this for?",
                    "description": "Performs TDD",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                },
                {
                    "recommendationID": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "???",
                    "description": "Run a daycare",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.1"
                }
            ]
        },
        {
            "substatementID": "4fa85f64-5717-4562-b3fc-2c963f66afa5",
            "substatement": "Can perform test driven development",
            "matches": [
                {
                    "recommendationID": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "???",
                    "description": "Run a daycare",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                },
                {
                    "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "what is this for?",
                    "description": "Performs TDD",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.1"
                }
            ]
        }
    ]
}

@describe('/match-table')
def _():
    
    # TODO mock calls to nameko
    @describe('when a match table exists')
    def _():

        my_pipeline = Pipeline()

        DB.session.add(my_pipeline)

        DB.session.commit()

        my_pipeline_id = my_pipeline.pipeline_id

        my_pipeline.match_table_data = match_table_dict


        @it('it accepts good data', skip=True)
        def _():
            nonlocal my_pipeline_id
            nonlocal my_pipeline
            DB.session.add(my_pipeline)
            print(my_pipeline)
            request_body = {
                'pipelineID': str(my_pipeline_id)
            }

            expected_response = {
                # "timestamp": "",
                "pipelineID": str(my_pipeline_id),
                "matchTable": match_table_dict
            }

            resp = application.post_json('/match-table', request_body)

            expect(resp.status_int).to(equal(200))

            expect(resp.json['matchTable']).to(equal(match_table_dict))

        # @it('rejects bad data')
        # def _():
        #     pass
