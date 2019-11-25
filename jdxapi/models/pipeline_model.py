from flask_sqlalchemy import SQLAlchemy
from jdxapi.app import DB
from jdxapi.utils.error import ApiError
from jdxapi.models.lookup_single_decorator import lookup_single_error_handler
from sqlalchemy import Integer, String, DateTime, Numeric, Column, func, Text, and_, ForeignKey, ARRAY
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import text as sa_text
import datetime
import uuid
from math import floor

junc_table = DB.Table('pipeline_framework_junc', DB.Model.metadata,
    Column('pipeline_id', UUID(as_uuid=True), ForeignKey('pipeline.pipeline_id')),
    Column('framework_id', UUID(as_uuid=True), ForeignKey('framework.framework_id'))
)

class Pipeline(DB.Model):
    __tablename__ = 'pipeline'

    pipeline_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        # default = generate_uuid4
        default=uuid.uuid4
    )
    user_token = Column(
        UUID(as_uuid=True),
        unique=True
    )

    frameworks = relationship(
        "Framework",
        secondary=junc_table
        # backref="pipelines"
    )

    # Future one-to-many?
    # job_description_id = Column(
    #     UUID(as_uuid=True),
    #     unique=True,
    #     # default = generate_uuid4
    #     default=uuid.uuid4
    # )

    file_name = Column(String)
    file_format = Column(String)  # optional?
    file_text = Column(Text)

    # define 'last_updated' to be populated with datetime.now()
    last_updated = Column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )
    
    match_table_data = Column(JSONB)
    match_table_selections = Column(JSONB)

    preview = Column(JSONB)

    primary_economic_activity = Column(String)
    job_title = Column(String)
    employer_name = Column(String)
    employer_overview = Column(String)
    employer_email = Column(String)
    employer_website = Column(String)
    employer_address = Column(String)
    employer_phone = Column(String)
    job_summary = Column(String)
    job_location = Column(String)
    job_location_type = Column(String)
    industry_code = Column(String)
    occupation_code = Column(String)
    employment_unit = Column(String)
    employer_identifier = Column(String)
    assessment = Column(String)
    employment_agreement = Column(String)
    job_term = Column(String)
    job_schedule = Column(String)
    work_hours = Column(String)
    requirements = Column(String)
    application_location_requirement = Column(String)
    citizenship_requirement = Column(String)
    physical_requirement = Column(String)
    sensory_requirement = Column(String)
    security_clearance_requirement = Column(String)
    special_commitment = Column(String)
    currency = Column(String)
    minimum = Column(String)
    maximum = Column(String)
    frequency = Column(String)
    incentive_compensation = Column(String)
    job_benefits = Column(ARRAY(String))
    date_posted = Column(String)
    valid_through = Column(String)
    job_openings = Column(String)

    def __repr__(self):
        return f'pipeline_id={self.pipeline_id}, user_token={self.user_token}, file_name={self.file_name}, file_format={self.file_format}, file_text={self.file_text}, last_updated={self.last_updated}'

    # # This will be used once we have OAuth
    # def user_is_authorized_to_access_pipeline(user_token, pipeline_id):
    #     # When given a user token and pipeline, this will
    #     # return True or False if that user owns the pipleine id
    #     query = DB.session.query(Pipeline).filter(
    #         and_(
    #             Pipeline.user_token==user_token,
    #             Pipeline.pipeline_id==pipeline_id
    #         )
    #     )
    #     results = query.all()
    #     return not not results

    @classmethod
    def create_new_pipeline(self, req_identity, file_name, file_format, file_text):
        new_pipeline = Pipeline(
            user_token=req_identity,
            file_name=file_name,
            file_format=file_format,
            file_text=file_text
        )

        DB.session.add(new_pipeline)
        DB.session.commit()

        return new_pipeline


    @classmethod    
    @lookup_single_error_handler('pipeline_id')
    def get_pipeline_from_id(self, pipeline_id):
        # Check if this pipeline ID even exists
        pipeline_query = DB.session.query(Pipeline).filter_by(pipeline_id=pipeline_id)
        pipeline = pipeline_query.one()
        return pipeline


    @classmethod    
    def check_if_match_table_data_exists(self, pipeline):
        match_table_data = pipeline.match_table_data
        if not match_table_data:
            raise ApiError('Data not in yet', 402) #TODO verify that its the processing command
        return match_table_data


    @classmethod    
    @lookup_single_error_handler('pipeline_id')
    def get_frameworks_from_pipeline_id(self, pipeline_id):
        pipeline_query = DB.session.query(Pipeline).filter_by(pipeline_id=pipeline_id)
        pipeline = pipeline_query.one()
        
        # attached_frameworks = pipeline.frameworks
        # frameworks = []
        # if len(attached_frameworks) == 0:
        #     pass

        # else if len(attached_frameworks) == 1:
        #     frameworks = [attached_frameworks.framework_name]

        # else:
        pipeline_frameworks = pipeline.frameworks

        if not pipeline_frameworks:
            raise ApiError(f"No frameworks found for pipeline_id '{pipeline_id}'", 402) #TODO verify that its the processing command

        frameworks = []
        for framework in pipeline_frameworks:
            frameworks.append(str(framework.framework_id))
        
        print(f'frameworks: {frameworks}')

        return frameworks

    @classmethod
    @lookup_single_error_handler('pipeline_id')
    def calculate_score(self, pipeline_id):
        pipeline_query = DB.session.query(Pipeline).filter_by(pipeline_id=pipeline_id)
        pipeline = pipeline_query.one()

        data = [
            pipeline.primary_economic_activity,
            pipeline.job_title,
            pipeline.employer_name,
            pipeline.employer_overview,
            pipeline.employer_email,
            pipeline.employer_website,
            pipeline.employer_address,
            pipeline.employer_phone,
            pipeline.job_summary,
            pipeline.job_location,
            pipeline.job_location_type,
            pipeline.industry_code,
            pipeline.occupation_code,
            pipeline.employment_unit,
            pipeline.employer_identifier,
            pipeline.assessment,
            pipeline.employment_agreement,
            pipeline.job_term,
            pipeline.job_schedule,
            pipeline.work_hours,
            pipeline.requirements,
            pipeline.application_location_requirement,
            pipeline.citizenship_requirement,
            pipeline.physical_requirement,
            pipeline.sensory_requirement,
            pipeline.security_clearance_requirement,
            pipeline.special_commitment,
            pipeline.currency,
            pipeline.minimum,
            pipeline.maximum,
            pipeline.frequency,
            pipeline.incentive_compensation,
            pipeline.job_benefits
        ]

        items_provided = len(data) - (data.count(None) + data.count(""))
        score = items_provided / len(data)

        print(data)
        print(items_provided)
        print(score)
        print(score*10)
        print(floor(score*10))

        messages = [
            'We do not have enough metadata to trust that sharing this file will be useful. We recommend that you go back and fill out more data fields.',
            'You have provided a good amount of metadata however search engines will be able to better understand your job if you go back and fill out more data fields.',
            'You have filled out nearly every single data field. Great!',
            'You have provided all the additional data we need. Great work!'
        ]

        explanations = {
            0: messages[0],
            1: messages[0],
            2: messages[0],
            3: messages[0],
            4: messages[0],
            5: messages[0],
            6: messages[0],
            7: messages[1],
            8: messages[1],
            9: messages[2],
            10: messages[3],
        }

        return score, explanations[floor(score*10)]