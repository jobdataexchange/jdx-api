from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
# from ..pocha_setup import application
# import uuid
from model_setup import setup_environment, restore_environment, get_app, get_db
import uuid
from jdxapi.models import *

setup_environment = before(setup_environment)
restore_environment = after(restore_environment)


@describe('framework') # TODO refactor out these to their own files
def _():

    DB = get_db()
    DB.session.expire_on_commit = False

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
    DB.session.commit()
    
    @describe('framework_type')
    def _():

        @it('does stuff', skip=True)
        def _():
            # expect(competency_framework).to()
            pass

    competency_framework = Framework(
        framework_type=competency_framework_type,
        framework_name="name1",
        framework_description="description",
        framework_uri="uri.com",
    )

    occupation_framework = Framework(
        framework_type=occupation_framework_type,
        framework_name="name2",
        framework_description="description",
        framework_uri="uri.com",
    )

    industry_framework = Framework(
        framework_type=industry_framework_type,
        framework_name="name3",
        framework_description="description",
        framework_uri="uri.com",
    )

    DB.session.add_all([
        competency_framework,
        occupation_framework,
        industry_framework
    ])


    DB.session.commit()
    
    @describe('framework')
    def _():

        @it('has a valid UUID')
        def _():
            DB.session.add(competency_framework)
            expect(isinstance(competency_framework.framework_id, uuid.UUID)).to(be_true)

    new_pipeline = Pipeline(
        user_token=uuid.uuid4(),
        file_name='test',
        file_format='test',
        file_text='test'
    )

    DB.session.add(new_pipeline)
    DB.session.commit()

    new_pipeline.frameworks.append(competency_framework)
    new_pipeline.frameworks.append(occupation_framework)
    new_pipeline.frameworks.append(industry_framework)
    DB.session.commit()

    @describe('pipline can recieve frameworks')
    def _():

        @it('does stuff', skip=True)
        def _():
            pass
