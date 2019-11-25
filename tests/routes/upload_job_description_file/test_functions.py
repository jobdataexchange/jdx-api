from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys

# get_req_identity(req)
# extract_text(file, file_format)
# get_length_of_job_description(file_data)
# communication_broker_call(thing, data)
# get_file_from_request(self, request)
# validate_file_in_request(self, request)
# allowed_file(self, filename)
# extract_file_properties(self, file)
# post(self)
# post(self)
from jdxapi.utils.functions import extract_text


@describe('texttract')
def _():

    @it('with good data')
    def _():
        with open('./tests/job-descriptions/testfile.txt', 'rb') as f:
            file_format = 'txt'
            data = extract_text(f, file_format)
            expect(data).to(equal("\ufeffHello world\n"))


@describe('upload job description util functions', skip=True)
def _():

    @describe('get_req_identity', skip=True)
    def _():

        @it('with good data', skip=True)
        def _():
            # req = 1
            # output = funcs.get_req_identity(req)
            # expect(output).to(equal(1))
            pass

    @describe('create_pipeline_id', skip=True)
    def _():

        @it('with good data', skip=True)
        def _():
            pass

    @describe('get_time_stamp', skip=True)
    def _():

        @it('with good data', skip=True)
        def _():
            pass

    @describe('get_length_of_job_description', skip=True)
    def _():

        @it('with good data', skip=True)
        def _():
            pass

