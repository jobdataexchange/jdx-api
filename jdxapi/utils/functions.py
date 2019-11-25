import textract
import tempfile
import uuid
from jdxapi.utils.error import ApiError
import jdxapi.utils.constants as c
from flask import jsonify
import os


def get_req_identity(req):
    # extract an identiy from the header token?
    return uuid.uuid4()


def get_length_of_job_description(file_data):
    return len(file_data)

import hashlib

def extract_text(file, file_name, file_format):
    # Given a file this will extract and return the text from it.
    # Save file
    print('extracting text...')
    # UPLOAD_FOLDER = './uploads'

    # file_name_and_type = f'{file_name}.{file_format}'
    # file_path = os.path.join(UPLOAD_FOLDER, file_name_and_type)

    with tempfile.NamedTemporaryFile(mode='w+b') as temp_file:
        
        file.save(temp_file)
        file.seek(0) # reset the given file head
        temp_file.seek(0)

        # try:
        file_text = textract.process(temp_file.name, 'utf-8', file_format)
        print(file_text)
        # except textract.exceptions.ShellError as e:
        # logger.error('{} - Could not convert Document ID {}!'.format(e, document_id))
        # raise ApiError('Could not extract text from provided file. Please try converting it to a .txt file and resubmitting.', 500)

    # Delete file
    # if os.path.exists(file_path):
    #     os.remove(file_path)
    # else:
    #     # logger.error(f'Was unable to find the saved uploaded file at "{file_path}"')
    #     print(f'Was unable to find the saved uploaded file at "{file_path}"')

    return file_text.decode('utf-8')

class RequestHandler():
    
    @classmethod
    def get_property(self, req, prop, required=True):
        """
        Given a prop and a required value, returns the value.
        """
        value = req.get(prop)
        if not required:
            return value

        if not value:
            raise ApiError(f"'{prop}' not found", 422)

        return value

    @classmethod
    def get_pipeline_id(self, req, required):
        return self.get_property(req, c.PIPELINE_ID, required)

    @classmethod
    def get_match_table_selections(self, req, required):
        return self.get_property(req, c.MATCH_TABLE_SELECTIONS, required)
    
    @classmethod
    def get_threshold(self, req, required):
        return self.get_property(req, c.THRESHOLD, required)

    
    @classmethod
    def get_primary_economic_activity(self, req):
        return self.get_property(req, "primaryEconomicActivity", False)


    @classmethod
    def get_employer_name(self, req):
        return self.get_property(req, "employerName", False)
    
    
    @classmethod
    def get_employer_overview(self, req):
        return self.get_property(req, "employerOverview", False)


    @classmethod
    def get_employer_email(self, req):
        return self.get_property(req, "employerEmail", False)


    @classmethod
    def get_employer_website(self, req):
        return self.get_property(req, "employerWebsite", False)


    @classmethod
    def get_employer_phone(self, req):
        return self.get_property(req, "employerPhone", False)


    @classmethod
    def get_employer_address(self, req):
        return self.get_property(req, "employerAddress", False)


    @classmethod
    def get_competency(self, req):
        return self.get_property(req, "competency", False)


    @classmethod
    def get_job_summary(self, req):
        return self.get_property(req, "jobSummary", False)


    @classmethod
    def get_industry_code(self, req):
        return self.get_property(req, "industryCode", False)


    @classmethod
    def get_occupation_code(self, req):
        return self.get_property(req, "occupationCode", False)


    @classmethod
    def get_job_location(self, req):
        return self.get_property(req, "jobLocation", False)


    @classmethod
    def get_job_location_type(self, req):
        return self.get_property(req, "jobLocationType", False)


    @classmethod
    def get_employment_unit(self, req):
        return self.get_property(req, "employmentUnit", False)


    @classmethod
    def get_employer_identifier(self, req):
        return self.get_property(req, "employerIdentifier", False)


    @classmethod
    def get_assessment(self, req):
        return self.get_property(req, "assessment", False)
  

    @classmethod
    def get_employment_agreement(self, req):
        return self.get_property(req, "employmentAgreement", False)


    @classmethod
    def get_job_term(self, req):
        return self.get_property(req, "jobTerm", False)


    @classmethod
    def get_job_schedule(self, req):
        return self.get_property(req, "jobSchedule", False)


    @classmethod
    def get_work_hours(self, req):
        return self.get_property(req, "workHours", False)


    @classmethod
    def get_requirements(self, req):
        return self.get_property(req, "requirements", False)


    @classmethod
    def get_application_location_requirement(self, req):
        return self.get_property(req, "applicationLocationRequirement", False)


    @classmethod
    def get_citizenship_requirement(self, req):
        return self.get_property(req, "citizenshipRequirement", False)


    @classmethod
    def get_physical_requirement(self, req):
        return self.get_property(req, "physicalRequirement", False)


    @classmethod
    def get_job_title(self, req):
        return self.get_property(req, "jobTitle", False)


    @classmethod
    def get_sensory_requirement(self, req):
        return self.get_property(req, "sensoryRequirement", False)


    @classmethod
    def get_security_clearance_requirement(self, req):
        return self.get_property(req, "securityClearanceRequirement", False)


    @classmethod
    def get_special_commitment(self, req):
        return self.get_property(req, "specialCommitment", False)


    @classmethod
    def get_currency(self, req):
        return self.get_property(req, "salaryCurrency", False)


    @classmethod
    def get_minimum(self, req):
        return self.get_property(req, "salaryMinimum", False)


    @classmethod
    def get_maximum(self, req):
        return self.get_property(req, "salaryMaximum", False)


    @classmethod
    def get_frequency(self, req):
        return self.get_property(req, "salaryFrequency", False)


    @classmethod
    def get_incentive_compensation(self, req):
        return self.get_property(req, "incentiveCompensation", False)

    #Array?
    @classmethod
    def get_job_benefits(self, req):
        return self.get_property(req, "jobBenefits", False)
  

    @classmethod
    def get_date_posted(self, req):
        return self.get_property(req, "datePosted", False)


    @classmethod
    def get_valid_through(self, req):
        return self.get_property(req, "validThrough", False)


    @classmethod
    def get_job_openings(self, req):
        return self.get_property(req, "jobOpenings", False)


    # @classmethod
    # def get_competencies(self, req):
    #     return self.get_property req[c.FRAMEWORKS].get(c.COMPETENCY)
    # @classmethod
    # def get_occupations(self, req):
    #     return self.get_property req[c.FRAMEWORKS].get(c.OCCUPATION)
    # @classmethod
    # def get_industries(self, req):
    #     return self.get_property req[c.FRAMEWORKS].get(c.INDUSTRY)

class ResponseHandler():

    @classmethod
    def create_response(self, response_data, status_code=200):
        response = jsonify(response_data)
        response.status_code = status_code
        return response

