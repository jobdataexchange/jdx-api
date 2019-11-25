from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from jdxapi.app import api, DB
from jdxapi.models import Pipeline
from jdxapi.utils.functions import RequestHandler, ResponseHandler
from jdxapi.utils.save_to_s3 import upload_jsp, upload_jsphr, upload_human_readable
from jdxapi.services.competensor import generate_job_schema_plus
import datetime
import jdxapi.utils.constants as c
import json
from jsphr_converter import convert_to_hr_and_save, convert_to_hr

@api.resource('/generate-job-schema-plus')
class GenerateJobSchemaPlus(LoggerResource):
    def post(self):
        req = request.get_json()
        pipeline_id = RequestHandler.get_pipeline_id(req, True)
        pipeline = Pipeline.get_pipeline_from_id(pipeline_id)

        job_schema_plus_file = generate_job_schema_plus(pipeline_id)

        schema, data = self.convert_jspf_to_human_readable(
            pipeline,
            job_schema_plus_file
        )

        resp_data = self.create_response_data(
            pipeline_id,
            job_schema_plus_file,
            schema,
            data
        )

        self.save_output(job_schema_plus_file, schema, data, pipeline_id)

        response = ResponseHandler.create_response(resp_data, 200)
        return response


    def save_output(self, job_schema_plus_file, schema, data, pipeline_id):
        now_string = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')

        jsp_file = f'/logs/output_jsp/{now_string}_{pipeline_id}_jsp.jsonld'
        human_readable_file = f'/logs/output_humanreadable/{now_string}_{pipeline_id}_human-readable.json'
        jsphr_file = f'/logs/output_jsphr/{now_string}_{pipeline_id}_jsphr.txt'

        self.save_json_to_file(jsp_file, job_schema_plus_file)

        jsphr = {
            "humanReadable": {
                "schema": schema,
                "data": data
            }
        }
        self.save_json_to_file(human_readable_file, jsphr)

        convert_to_hr_and_save(jsphr, jsphr_file)

        upload_jsp(jsp_file)
        upload_jsphr(jsphr_file)
        upload_human_readable(human_readable_file)


    def save_json_to_file(self, filename, json_data):
        with open(filename, 'w+') as f:
            json.dump(json_data, f, indent=4)


    def create_response_data(self, pipeline_id, job_schema_plus_file, schema, data):
        resp_data = {
            c.PIPELINE_ID: str(pipeline_id),
            c.TIMESTAMP: str(datetime.datetime.now()),
            "jobSchemaPlusFile": dict(job_schema_plus_file),
            "humanReadable": {
                "schema": schema,
                "data": data
            }
        }

        return resp_data


    def convert_jspf_to_human_readable(self, pipeline, jsonld):
        print(jsonld)
        # print(type(job_schema_plus_file))        
        
        ORG = 0
        POSTING = 1
        graph = jsonld['@graph']

        job_title = graph[POSTING]['schema:title']['en-US']
        employer_name = graph[ORG]['schema:legalName']['en-US']
        employer_email = graph[ORG]['email']
        employer_address = graph[ORG]['schema:address']['streetAddress']
        employer_website = graph[ORG]['url']
        employer_phone = graph[ORG]['telephone']
        employer_overview = graph[ORG]['jdx:employerOverview']['en-US']

        job_summary = graph[POSTING]['schema:description']['en-US']
        primary_economic_activity = graph[POSTING]['schema:industry']['en-US']
        industry_code = graph[ORG]['jdx:industryCode']['termCode']
        occupation_code = graph[ORG]['schema:occupationalCategory']['termCode']

        job_location = graph[POSTING]["schema:jobLocation"]["address"]["schema:streetAddress"]
        job_location_type = graph[POSTING]["schema:jobLocationType"]['en-US']
        employment_unit = graph[POSTING]['jdx:employmentUnit']['name']
        employer_identifier = graph[POSTING]['jdx:positionID']

        assessment = graph[POSTING]['jdx:requiredAssessment']["description"]

        employment_agreement = graph[POSTING]['jdx:jobAgreement']['name']
        job_term = graph[POSTING]['jdx:jobTerm']['name']
        work_hours = graph[POSTING]['jdx:workHours']['name']
        job_schedule = graph[POSTING]['jdx:jobSchedule']['name']

        credentials = graph[POSTING]['jdx:requiredCredential']['description']['en-US']

        citizenship_requirement = graph[POSTING]['jdx:citizenshipRequirement']['name']['en-US']
        physical_requirement = graph[POSTING]['jdx:physicalRequirement']['en-US']
        sensory_requirement = graph[POSTING]['jdx:sensoryRequirement']['en-US']
        security_clearance_requirement = graph[POSTING]['jdx:securityClearanceRequirement']['en-US']
        special_commitment = graph[POSTING]['jdx:specialCommitment']['en-US']

        minimum = graph[POSTING]['schema:baseSalary']['schema:minValue']
        maximum = graph[POSTING]['schema:baseSalary']['schema:maxValue']
        frequency = graph[POSTING]['schema:baseSalary']['payCycleInterval']['name']['en-US']
        incentive_compensation = graph[POSTING]['schema:incentiveCompensation']['en-US']

        graph_benefits_list = graph[POSTING]['schema:jobBenefits']
        benefits_list = [item['name']['en-US'] for item in graph_benefits_list]

        application_location_requirement = graph[POSTING]['jdx:applicantLocationRequirement']["name"]

        # Add competencies
        _jsp_competencies = graph[POSTING]["jdx:competency"]
        competencies = [item['schema:description']['en-US'].strip('\n').replace('\n', ' ').replace('\t', ' ').strip() for item in _jsp_competencies]

        # Job Posting data
        date_posted = graph[POSTING]['schema:datePosted']
        valid_through = graph[POSTING]['schema:validThrough']
        job_openings = graph[POSTING]['totalJobOpenings']
        
        schema = [
            'Job Title',
            'Employer Name',
            'Employer Email',
            'Employer Website',
            'Employer Phone',
            'Employer Address',
            'Employer Identifier',
            'Employer Overview',
            'Primary Economic Activity',
            'Industry Code',
            'Occupation Code',
            'Job Summary',
            'Job Location',
            'Job Location Type',
            'Employment Unit',
            'Employment Agreement',
            'Competencies',
            'Assessment',
            'Job Term',
            'Work Hours',
            'Job Schedule',
            'Credentials',
            'Application Location Requirement',
            'Citizenship Requirement',
            'Physical Requirement',
            'Sensory Requirement',
            'Security Clearance Requirement',
            'Special Commitment',
            'Salary Minimum',
            'Salary Maximum',
            'Frequency',
            'Incentive Compensation',
            'Benefits List',
            'Date Posted',
            'Valid Through',
            'Job Openings'
        ]

        human_readable_data = {
            'Job Title': job_title,
            'Employer Name': employer_name,
            'Employer Email': employer_email,
            'Employer Address': employer_address,
            'Employer Website': employer_website,
            'Employer Phone': employer_phone,
            'Employer Identifier': employer_identifier,
            'Employer Overview': employer_overview,
            'Primary Economic Activity': primary_economic_activity,
            'Industry Code': industry_code,
            'Occupation Code': occupation_code,
            'Job Summary': job_summary,
            'Job Location': job_location,
            'Job Location Type': job_location_type,
            'Employment Unit': employment_unit,
            'Employment Agreement': employment_agreement,
            'Competencies': competencies,
            'Assessment': assessment,
            'Job Term': job_term,
            'Work Hours': work_hours,
            'Job Schedule': job_schedule,
            'Credentials': credentials,
            'Application Location Requirement': application_location_requirement,
            'Citizenship Requirement': citizenship_requirement,
            'Physical Requirement': physical_requirement,
            'Sensory Requirement': sensory_requirement,
            'Security Clearance Requirement': security_clearance_requirement,
            'Special Commitment': special_commitment,
            'Salary Minimum': str(minimum),
            'Salary Maximum': str(maximum),
            'Frequency': frequency,
            'Incentive Compensation': incentive_compensation,
            'Benefits List': benefits_list,
            'Date Posted': date_posted,
            'Valid Through': valid_through,
            'Job Openings': job_openings,
        }

        assert(len(schema) == len(human_readable_data))
        data_dict = {
            "schema": str(schema),
            "data": str(human_readable_data)
        }

        print(data_dict)
        return schema, human_readable_data
