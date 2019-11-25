from flask import request, jsonify
from jdxapi.utils.logger_resource import LoggerResource
from jdxapi.app import api, DB
from jdxapi.models import Pipeline
from jdxapi.utils.functions import RequestHandler
from jdxapi.utils.error import ApiError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import jdxapi.utils.constants as c


@api.resource("/upload-job-description-context")
class UploadJobDescriptionContext(LoggerResource):
    
    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        pipeline = Pipeline.get_pipeline_from_id(pipeline_id)
        
        self.extract_and_save_to_pipeline(req, pipeline)

        resp_data = self.create_response_data(pipeline)
        response = self.make_response(resp_data)
        return response

    def extract_and_save_to_pipeline(self, req, pipeline):
        job_title = RequestHandler.get_job_title(req)
        primary_economic_activity = RequestHandler.get_primary_economic_activity(req)
        employer_name = RequestHandler.get_employer_name(req)
        employer_overview = RequestHandler.get_employer_overview(req)
        employer_email = RequestHandler.get_employer_email(req)
        employer_website = RequestHandler.get_employer_website(req)
        employer_address = RequestHandler.get_employer_address(req)
        employer_phone = RequestHandler.get_employer_phone(req)
        competency = RequestHandler.get_competency(req)
        job_summary = RequestHandler.get_job_summary(req)
        industry_code = RequestHandler.get_industry_code(req)
        occupation_code = RequestHandler.get_occupation_code(req)
        job_location = RequestHandler.get_job_location(req)
        job_location_type = RequestHandler.get_job_location_type(req)
        employment_unit = RequestHandler.get_employment_unit(req)
        employer_identifier = RequestHandler.get_employer_identifier(req)
        assessment = RequestHandler.get_assessment(req)
        employment_agreement = RequestHandler.get_employment_agreement(req)
        job_term = RequestHandler.get_job_term(req)
        job_schedule = RequestHandler.get_job_schedule(req)
        work_hours = RequestHandler.get_work_hours(req)
        requirements = RequestHandler.get_requirements(req)
        application_location_requirement = RequestHandler.get_application_location_requirement(req)
        citizenship_requirement = RequestHandler.get_citizenship_requirement(req)
        physical_requirement = RequestHandler.get_physical_requirement(req)
        sensory_requirement = RequestHandler.get_sensory_requirement(req)
        security_clearance_requirement = RequestHandler.get_security_clearance_requirement(req)
        special_commitment = RequestHandler.get_special_commitment(req)
        currency = RequestHandler.get_currency(req)
        minimum = RequestHandler.get_minimum(req)
        maximum = RequestHandler.get_maximum(req)
        frequency = RequestHandler.get_frequency(req)
        incentive_compensation = RequestHandler.get_incentive_compensation(req)
        job_benefits = RequestHandler.get_job_benefits(req)
        date_posted = RequestHandler.get_date_posted(req)
        valid_through = RequestHandler.get_valid_through(req)
        job_openings = RequestHandler.get_job_openings(req)

        pipeline.job_title = job_title
        pipeline.primary_economic_activity = primary_economic_activity
        pipeline.employer_name = employer_name
        pipeline.employer_overview = employer_overview
        pipeline.employer_email = employer_email
        pipeline.employer_website = employer_website
        pipeline.employer_address = employer_address
        pipeline.employer_phone = employer_phone
        pipeline.competency = competency
        pipeline.job_summary = job_summary
        pipeline.industry_code = industry_code
        pipeline.occupation_code = occupation_code
        pipeline.job_location = job_location
        pipeline.job_location_type = job_location_type
        pipeline.employment_unit = employment_unit
        pipeline.employer_identifier = employer_identifier
        pipeline.assessment = assessment
        pipeline.employment_agreement = employment_agreement
        pipeline.job_term = job_term
        pipeline.job_schedule = job_schedule
        pipeline.work_hours = work_hours
        pipeline.requirements = requirements
        pipeline.application_location_requirement = application_location_requirement
        pipeline.citizenship_requirement = citizenship_requirement
        pipeline.physical_requirement = physical_requirement
        pipeline.sensory_requirement = sensory_requirement
        pipeline.security_clearance_requirement = security_clearance_requirement
        pipeline.special_commitment = special_commitment
        pipeline.currency = currency
        pipeline.minimum = minimum
        pipeline.maximum = maximum
        pipeline.frequency = frequency
        pipeline.incentive_compensation = incentive_compensation
        pipeline.job_benefits = job_benefits
        pipeline.date_posted = date_posted
        pipeline.valid_through = valid_through
        pipeline.job_openings = job_openings
        
        DB.session.commit()


    def create_response_data(self, pipeline):
        resp_data = {
            c.PIPELINE_ID: str(pipeline.pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now()),
            "primaryEconomicActivity": pipeline.primary_economic_activity,
            "employerName": pipeline.employer_name,
            "employerOverview": pipeline.employer_overview,
            "employerEmail": pipeline.employer_email,
            "employerWebsite": pipeline.employer_website,
            "employerAddress": pipeline.employer_address,
            "employerPhone": pipeline.employer_phone,
            "competency": pipeline.competency,
            "jobSummary": pipeline.job_summary,
            "industryCode": pipeline.industry_code,
            "occupationCode": pipeline.occupation_code,
            "jobLocation": pipeline.job_location,
            "jobLocationType": pipeline.job_location_type,
            "employmentUnit": pipeline.employment_unit,
            "employerIdentifier": pipeline.employer_identifier,
            "assessment": pipeline.assessment,
            "employmentAgreement": pipeline.employment_agreement,
            "jobTitle": pipeline.job_title,
            "jobTerm": pipeline.job_term,
            "jobSchedule": pipeline.job_schedule,
            "workHours": pipeline.work_hours,
            "requirements": pipeline.requirements,
            "applicationLocationRequirement": pipeline.application_location_requirement,
            "citizenshipRequirement": pipeline.citizenship_requirement,
            "physicalRequirement": pipeline.physical_requirement,
            "sensoryRequirement": pipeline.sensory_requirement,
            "securityClearanceRequirement": pipeline.security_clearance_requirement,
            "specialCommitment": pipeline.special_commitment,
            "salaryJobTitle": pipeline.job_title,            
            "salaryCurrency": pipeline.currency,
            "salaryMinimum": pipeline.minimum,
            "salaryMaximum": pipeline.maximum,
            "salaryFrequency": pipeline.frequency,
            "incentiveCompensation": pipeline.incentive_compensation,
            "jobBenefits": pipeline.job_benefits,
            "datePosted": pipeline.date_posted,
            "validThrough": pipeline.valid_through,
            "jobOpenings": pipeline.job_openings
        }

        return resp_data
        

    def make_response(self, resp_data):
        response = jsonify(resp_data)
        response.status_code = 200
        return response
