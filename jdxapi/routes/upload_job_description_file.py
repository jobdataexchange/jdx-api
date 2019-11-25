from jdxapi.app import api, DB, ApiError, app
from jdxapi.models import Pipeline
from jdxapi.utils.logger_resource import LoggerResource
from flask import request, jsonify
from werkzeug.utils import secure_filename
from jdxapi.utils.functions import get_req_identity, extract_text, get_length_of_job_description, RequestHandler, ResponseHandler
import uuid
import datetime
import logging
import os


@api.resource("/upload-job-description-file")
class UploadJobDescriptionFile(LoggerResource):

    ALLOWED_EXTENSIONS = set(['txt', 'doc', 'docx'])
    UPLOAD_FOLDER = '/logs/input_jd'

    def post(self):
        self.validate_file_in_request(request)
        
        file = self.get_file_from_request(request)   
        file_name, file_format = self.extract_file_properties(file)
        
        file_text = extract_text(file, file_name, file_format)

        converted_length = get_length_of_job_description(file_text)

        req_identity = get_req_identity(request)

        new_pipeline = Pipeline.create_new_pipeline(req_identity, file_name, file_format, file_text)
        pipeline_id = new_pipeline.pipeline_id

        self.save_file(file, file_name, file_format, pipeline_id)

        resp_data = self.create_response_data(pipeline_id, new_pipeline, converted_length)
        response = ResponseHandler.create_response(resp_data, 200)
        return response


    def get_file_from_request(self, request):
        return request.files['file']


    def validate_file_in_request(self, request):
        ## Validates requirements for the file
        # Returns either a status code for a failure or None for success
        logging.info(request.files)
        if 'file' not in request.files:
            # flash('No file part')
            raise ApiError("submit to 'file' field")
        
        file = self.get_file_from_request(request)

        if not file:
            raise ApiError("No file found")

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            # flash('No selected file')
            raise ApiError("No selected file")

        if not self.allowed_file(file.filename):
            raise ApiError(f'Only the following file types allowed, {self.ALLOWED_EXTENSIONS}')
        

    def allowed_file(self, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS


    def extract_file_properties(self, file):
        # Given a file, returns [file_name, file_format]
        full_file_name = secure_filename(file.filename)
        return full_file_name.lower().rsplit('.', 1)


    def save_file(self, file, file_name, file_format, pipeline_id):
        now_string = datetime.datetime.now().strftime('%m-%d-%Y_%H-%M-%S')

        # try:
        file.save(
            os.path.join(
                self.UPLOAD_FOLDER,
                f'{now_string}_{str(pipeline_id)}_{file_name}.{file_format}'
            )
        )
        # except:
        #     logger = logging.getLogger('inputoutput')
        #     logger.exception('Could not save uploaded job description:')


    def create_response_data(self, pipeline_id, new_pipeline, converted_length):
        resp_data = {
            "pipelineID": str(pipeline_id),
            "timestamp": str(datetime.datetime.now()),
            "convertedLength": int(converted_length),
            "fileText": str(new_pipeline.file_text)
        }
        return resp_data
