from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
# from ..pocha_setup import application
# import uuid
from model_setup import setup_environment, restore_environment, get_app, get_db

from jdxapi.models import *

setup_environment = before(setup_environment)
restore_environment = after(restore_environment)


@describe('framework model')
def _():

    # @describe('Pipeline.user_is_authorized_to_access_pipeline')
    # def _():

    #     testDB = get_db()

    #     auth_user_token = uuid.uuid4()
    #     unauth_user_token = uuid.uuid4()

    #     new_pipeline = pipeline_model.Pipeline(
    #         user_token=auth_user_token,
    #         file_name="file_name",
    #         file_format="file_format",
    #         file_text="file_text"
    #     )

    #     testDB.session.add(new_pipeline)
    #     testDB.session.commit()

    #     pipeline_id = new_pipeline.pipeline_id

    #     @it('passes when a user access their pipeline')
    #     def _():            
    #         result = pipeline_model.Pipeline.user_is_authorized_to_access_pipeline(
    #             auth_user_token, 
    #             pipeline_id
    #         )

    #         expect(result).to(equal(True))

    #     @it('fails when a user access someone elses pipeline')
    #     def _():
    #         result = pipeline_model.Pipeline.user_is_authorized_to_access_pipeline(
    #             unauth_user_token, 
    #             pipeline_id
    #         )

    #         expect(result).to(equal(False))


    @it('does stuff', skip=True)
    def _():
        pass
