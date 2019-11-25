import uuid
import os
import sys
from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
# import jdxapi.routes.upload_job_description as utils

# from model_setup import setup_environment, restore_environment, get_app, get_db
from ...pocha_setup import application, DB

from jdxapi.models import FrameworkRecommendation, Pipeline, Framework, FrameworkType
import datetime


@describe('/framework-selections')
def _():

    @describe('when a job description file has been uploaded')
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

        @describe('and framework recommendations have been generated')
        def _():

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

            DB.session.add_all([
                first_recommendation,
                second_recommendation
            ])
            DB.session.commit()



            # prepopulating db
            competency_framework_type = FrameworkType(
                framework_type="competency"
            )

            occupation_framework_type = FrameworkType(
                framework_type="occupation"
            )

            industry_framework_type = FrameworkType(
                framework_type="industry"
            )

            DB.session.add_all([
                competency_framework_type,
                occupation_framework_type,
                industry_framework_type
            ])

            competency_framework = Framework(
                framework_type=competency_framework_type,
                framework_name="name7",
                framework_description="description",
                framework_uri="uri.com",
            )

            occupation_framework = Framework(
                framework_type=occupation_framework_type,
                framework_name="name8",
                framework_description="description",
                framework_uri="uri.com",
            )

            industry_framework = Framework(
                framework_type=industry_framework_type,
                framework_name="name9",
                framework_description="description",
                framework_uri="uri.com",
            )

            DB.session.add_all([
                competency_framework,
                occupation_framework,
                industry_framework
            ])
            DB.session.commit()

            @it('it accepts good data')
            def _():                
                request_body = {
                    "pipelineID": str(my_pipeline_id),
                    "frameworks": {
                        "competency": [
                            {
                                "frameworkID": str(competency_framework.framework_id)
                            }
                        ],
                        "occupation": [
                            {
                                "frameworkID": str(occupation_framework.framework_id)
                            }
                        ],
                        "industry": [
                            {
                                "frameworkID": str(industry_framework.framework_id)
                            }
                        ]
                    }
                }
                
                # print(expected_body)
                resp = application.post_json('/framework-selections', request_body)

                expect(resp.status_int).to(equal(200))                
                # expect(resp.json).to(equal(request_body))
            
            @it('when given only competencies its ok')
            def _():
                DB.session.add_all([
                    new_pipeline,
                    first_recommendation,
                    second_recommendation,
                    competency_framework_type,
                    occupation_framework_type,
                    industry_framework_type,
                    competency_framework,
                    occupation_framework,
                    industry_framework
                ])           
                request_body = {
                    "pipelineID": str(my_pipeline_id),
                    "frameworks": {
                        "competency": [
                            {
                                "frameworkID": str(competency_framework.framework_id)
                            },
                            {
                                "frameworkID": str(competency_framework.framework_id)
                            }
                        ]
                    }
                }
                
                # print(expected_body)
                resp = application.post_json('/framework-selections', request_body)

                expect(resp.status_int).to(equal(200))                
                # expect(resp.json).to(equal(request_body))
            
            @it('when given no frameworks it errors')
            def _():
                nonlocal new_pipeline
                DB.session.add_all([
                    new_pipeline,
                    first_recommendation,
                    second_recommendation,
                    competency_framework_type,
                    occupation_framework_type,
                    industry_framework_type,
                    competency_framework,
                    occupation_framework,
                    industry_framework
                ])

                request_body = {
                    "pipelineID": str(my_pipeline_id),
                    "frameworks": {}
                }
                
                resp = application.post_json('/framework-selections', request_body, expect_errors=True)

                expect(resp.status_int).to(equal(422))
                        
            @it('when given no pipeline it errors')
            def _():
                nonlocal new_pipeline
                DB.session.add_all([
                    new_pipeline,
                    first_recommendation,
                    second_recommendation,
                    competency_framework_type,
                    occupation_framework_type,
                    industry_framework_type,
                    competency_framework,
                    occupation_framework,
                    industry_framework
                ])

                request_body = {
                    "frameworks": {
                        "competency": [
                            {
                                "frameworkID": str(competency_framework.framework_id)
                            }
                        ],
                        "occupation": [
                            {
                                "frameworkID": str(occupation_framework.framework_id)
                            }
                        ],
                        "industry": [
                            {
                                "frameworkID": str(industry_framework.framework_id)
                            }
                        ]
                    }
                }
                
                resp = application.post_json('/framework-selections', request_body, expect_errors=True)

                expect(resp.status_int).to(equal(422))
                


    @describe('when a job description file has NOT been uploaded')
    def _():

        @it("POST with good data", skip=True)
        def _():
            pass
    

        # @it("POST with bad data", skip=True)
        # def _():
        #     pass
