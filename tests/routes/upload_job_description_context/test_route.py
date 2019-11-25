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


@describe('/upload-job-description-context')
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


        @it('it accepts good data')
        def _():
            # jobOverview
            #     title
            #     Description
            #     industry
            #     industryCode
            #     occupationCategory
            #     jobLocation
            #     jobLocationType
            #     employmentUnit
            #     positionID | postingID
            # employmentRelationship
            #     jobAgreement
            #     jobTerm
            #     jobSchedule
            #     workHours
            # competencyRelatedInformation
            #     requiredAssessment
            # hiringRequirements
            #     applicantLocationRequirement
            #     citizenshipRequirement
            #     physicalRequirement
            #     sensoryRequirement
            #     securityClearanceRequirement
            #     specialCommitment
            #     incentiveCompensation
            #     jobBenefits
            #     datePosted
            #     validThrough
            #     totalJobOpenings
            # education
            #     requiredCredential
            #     preferredCredential
            #     equivalentCredential
            #     minimumCredential
            #     requiredEducation
            #     preferredEducation
            #     equivalentEducation
            #     minimumEducation
            #     requiredExperience
            #     preferredExperience
            #     equivalentExperience
            #     minimumExperience
            # compensationInformation
            #     currency
            #     baseSalary
            request_body = {
                "pipelineID": str(my_pipeline_id),
                "context":
                    "title": "ACME cyber programmer"
                    "description": "aasdfasdf asdf asdf asdf  asdf asdf  asdfasdf asdf asdf asdf asfd."
                    "industry": "qwer"
                    "industryCode": "qwer"
                    "occupationCategory": "qwer"
                    "jobLocation": "qwer"
                    "jobLocationType": "qwer"
                    "employmentUnit": "qwer"
                    "positionID": "internal-id-string"
                    "jobAgreement": "qwer"
                    "jobTerm": "qwer"
                    "jobSchedule": "qwer"
                    "workHours": "qwer"
                    "requiredAssessment": "qwer"
                    "applicantLocationRequirement": "qwer"
                    "citizenshipRequirement": "qwer"
                    "physicalRequirement": "qwer"
                    "sensoryRequirement": "qwer"
                    "securityClearanceRequirement": "qwer"
                    "specialCommitment": "qwer"
                    "incentiveCompensation": "qwer"
                    "jobBenefits": "qwer"
                    "datePosted": "qwer"
                    "validThrough": "qwer"
                    "totalJobOpenings": "qwer"
                    "requiredCredential": "qwer"
                    "preferredCredential": "qwer"
                    "equivalentCredential": "qwer"
                    "minimumCredential": "qwer"
                    "requiredEducation": "qwer"
                    "preferredEducation": "qwer"
                    "equivalentEducation": "qwer"
                    "minimumEducation": "qwer"
                    "requiredExperience": "qwer"
                    "preferredExperience": "qwer"
                    "equivalentExperience": "qwer"
                    "minimumExperience": "qwer"
                    "currency": "qwer"
                    "baseSalary": "qwer"
            }

            request_body = {
                "pipelineID": str(my_pipeline_id),
                "primaryEconomicActivity": "Making and selling software products",
                "jobLocation": {
                    "name": "ACME Fairfax",
                    "description": "A place where software is built",
                    "faxNumber": "+17039999999",
                    "telephone": "+17039999999",
                    "address": {
                        "name": "ACME Fairfax",
                        "streetAddress": "101 Acme Way",
                        "locality": "Fairfax",
                        "region": "Virgina",
                        "country": "United States of America",
                        "postalCode": 22032
                    },
                    "geo": {
                        "latitude": 123.4554534534,
                        "longitude": 223.4554534534
                    }
                },
                "occupationCategory": {
                    "name": "SOC",
                    "description": "Standardized Occupation Code, for use in the US",
                    "termCode": "15-1131.00",
                    "definedTermSet": "Standard Occupational Classification system"
                },
                "industryCategory": {
                    "name": "SOC",
                    "description": "Standardized Occupation Code, for use in the US",
                    "termCode": "15-1131.00",
                    "definedTermSet": "Standard Occupational Classification system"
                }
                # "responsibilties": [
                #     "walking the dog",
                #     "writing code",
                #     "attending meetings"
                # ]
            }

            # expected_body = request_body
            # print(expected_body)
            resp = application.post_json('/upload-job-description-context', request_body)

            expect(resp.status_int).to(equal(200))
            
            expect(resp.json).to(have_keys(request_body))
        
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
