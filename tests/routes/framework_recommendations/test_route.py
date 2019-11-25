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


@describe('/framework-recommendations')
def _():

    @describe('when there are two recommendations')
    def _():

        new_pipeline = Pipeline(
            user_token=uuid.uuid4(),
            file_name='test',
            file_format='test',
            file_text='test'
        )

        DB.session.add(new_pipeline)
        DB.session.commit()

        my_pipeline_id = new_pipeline.pipeline_id

        first_recommendation = FrameworkRecommendation(
            user_token=uuid.uuid4(),
            value='1',
            valid_until=datetime.datetime.now(),
            pipeline_id=my_pipeline_id,
            user_type='test',
            object_type='test',
            statistic_type='test',
            metric_class='test',
            total_number=1234,
            recommended_content='test'
        )

        second_recommendation = FrameworkRecommendation(
            user_token=uuid.uuid4(),
            value='2',
            valid_until=datetime.datetime.now(),
            pipeline_id=my_pipeline_id,
            user_type='test',
            object_type='test',
            statistic_type='test',
            metric_class='test',
            total_number=1234,
            recommended_content='test'
        )

        DB.session.add(first_recommendation)
        DB.session.add(second_recommendation)
        DB.session.commit()

        # TODO mock calls to nameko
        @it('returns boths', skip=True)
        def _():
            request_body = {
                'pipelineID': str(my_pipeline_id)
            }

            # expected_body = [
            #     {
            #         'value': '1',
            #         'validUntil': '2019-05-17 17:19:02.206799',
            #         'metrics': {
            #             'userType': 'test',
            #             'pipelineID': 'ca22f6a5-7cfd-4ca8-9170-aabc528e80d1',
            #             'objectType': 'test',
            #             'statisticsType': 'test',
            #             'extraInfo': {
            #                 'totalNumber': '1234',
            #                 'recommendedContent': 'test'
            #             },
            #         'metricClass': 'test'}
            #     },{
            #         'value': '2', 
            #         'validUntil': '2019-05-17 17:19:02.206884', 
            #         'metrics': {
            #             'userType': 'test', 
            #             'pipelineID': 'ca22f6a5-7cfd-4ca8-9170-aabc528e80d1', 
            #             'objectType': 'test', 
            #             'statisticsType': 'test', 
            #             'extraInfo': {
            #                 'totalNumber': '1234', 
            #                 'recommendedContent': 'test'
            #             }, 
            #         'metricClass': 'test'}
            #     }
            # ]

            resp = application.post_json('/framework-recommendations', request_body)

            expect(resp.status_int).to(equal(200))
            
            response_count = len(resp.json['frameworkRecommendations'])
            expect(response_count).to(equal(2))

            # expect(resp.json).to(equal(expected_response))
            # expect(resp.json).to(have_keys(expected_response))

        
        # @it('')
        # def _():
        #     pass


    @it("POST with good data", skip=True)
    def _():
        pass
    
    @it("POST with bad data", skip=True)
    def _():
        pass
