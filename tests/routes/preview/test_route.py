import uuid
import os
import sys
from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
# import jdxapi.routes.upload_job_description as utils

# from model_setup import setup_environment, restore_environment, get_app, get_db
from ...pocha_setup import application, DB

from jdxapi.models import FrameworkRecommendation, Pipeline
import datetime


@describe('/preview')
def _():

    @describe('when a job description file has been uploaded')
    def _():

        new_pipeline = Pipeline(
            user_token=uuid.uuid4(),
            file_name='test',
            file_format='test',
            file_text='test',
            preview={"hello": "world"}
        )

        DB.session.add(new_pipeline)
        DB.session.commit()

        my_pipeline_id = new_pipeline.pipeline_id


        @it('it accepts good data', skip=True)
        def _():
            request_body = {"pipelineID": str(my_pipeline_id)}
            expected_body = {
                "pipelineID": str(my_pipeline_id),
                # "preview": {
                #     "hello": "world"
                # }
            }
            resp = application.post_json('/preview', request_body)

            expect(resp.status_int).to(equal(200))
            
            expect(resp.json).to(have_keys(expected_body))
        
        # @it('rejects bad data')
        # def _():
        #     pass

    @describe('when a job description file has NOT been uploaded')
    def _():

        @it("POST with good data", skip=True)
        def _():
            pass
    

        # @it("POST with bad data", skip=True)
        # def _():
        #     pass
