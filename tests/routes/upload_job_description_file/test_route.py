import uuid
import os
import sys
from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
from ...pocha_setup import application
# import jdxapi.routes.upload_job_description as utils


@describe('/upload-job-description-file')
def _():

    # TODO refactor to unit tests for extract_text
    @it("POST with .txt")
    def _():
        upload_file_path = './tests/job-descriptions/testfile.txt'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)]
        )

        expect(resp.status_int).to(equal(200))
        expect(resp.content_type).to(equal('application/json'))

    @it("POST with sample .doc")
    def _():
        upload_file_path = './tests/job-descriptions/Sales Manager - Vitafoods Europe - Sep 2011.doc'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)]
        )

        expect(resp.status_int).to(equal(200))
        expect(resp.content_type).to(equal('application/json'))
    
    # TODO THIS WILL FAIL AND IS A KNOWN BUG
    @it("POST with a small .doc made on OpenOffice", skip=True) 
    def _():
        upload_file_path = './tests/job-descriptions/testfile.doc'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)]
        )

        expect(resp.status_int).to(equal(200))
        expect(resp.content_type).to(equal('application/json'))

    
    @it("POST with test .docx")
    def _():

        upload_file_path = './tests/job-descriptions/testfile.docx'

        # expected_response = {
            # "pipelineID": "randnums",
            # "timestamp": "time",
            # "jobDescriptionID": "jobid",
            # "convertedLength": 12345
        # }

        # # Stubs
        # utils.get_req_identity = lambda x : uuid.uuid4()
        # utils.create_pipeline_id = lambda x : 'pipeline'
        # utils.get_time_stamp = lambda : 'time'
        # utils.get_job_description_id = lambda : 'jobid'
        # utils.get_length_of_job_description = lambda x : 12345

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)]
        )

        # expect({'bar': 0, 'baz': 1}).to(have_key('bar', None))
        # expect({'bar': 0, 'baz': 1}).to(have_keys(bar=0, baz=1))
        # expect({'bar': 0, 'baz': 1}).not_to(have_keys({'foo': 0, 'foobar': 1}))
        # print(resp)
        expect(resp.status_int).to(equal(200))
        expect(resp.content_type).to(equal('application/json'))
        expect(resp.json).to(have_keys('pipelineID', 'convertedLength', 'fileText', 'timestamp'))
        # expect(resp.json).to(equal(expected_response))
        # expect(resp.json).to(have_keys(expected_response))

    @it("POST with sample .docx")
    def _():

        upload_file_path = './tests/job-descriptions/Licensed Practical Nurse Job Description V4.docx'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)],
            expect_errors=True
        )

        expect(resp.status_int).to(equal(200))
        expect(resp.content_type).to(equal('application/json'))

    @it("POST without 'file'")
    def _():
        upload_file_path = './tests/job-descriptions/unsupported.pdf'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('asdf', upload_file_path)],
            expect_errors=True
        )
        
        expect(resp.status_int).to(equal(400))


    @it("POST with unsupported pdf")
    def _():
        upload_file_path = './tests/job-descriptions/unsupported.pdf'

        resp = application.post(
            '/upload-job-description-file',
            upload_files=[('file', upload_file_path)],
            expect_errors=True
        )
        
        expect(resp.status_int).to(equal(400))

    @it("POST with nothing")
    def _():
        resp = application.post(
            '/upload-job-description-file',
            expect_errors=True
        )

        expect(resp.status_int).to(equal(400))
