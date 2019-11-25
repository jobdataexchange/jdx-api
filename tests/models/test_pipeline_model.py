from pocha import describe, it, before, after
from expects import expect, equal, be_none, be, be_above, be_true, have_keys
# from ..pocha_setup import application
# import uuid
from model_setup import setup_environment, restore_environment, get_app, get_db
from jdxapi.models import Pipeline, FrameworkType, Framework
import uuid

setup_environment = before(setup_environment)
restore_environment = after(restore_environment)

match_table_dict = {
    "matchTable": [
        {
            "substatementID": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
            "substatement": "Can perform test driven development",
            "matches": [
                {
                    "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "what is this for?",
                    "description": "Performs TDD",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                },
                {
                    "recommendationID": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "???",
                    "description": "Run a daycare",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.1"
                }
            ]
        },
        {
            "substatementID": "4fa85f64-5717-4562-b3fc-2c963f66afa5",
            "substatement": "Can perform test driven development",
            "matches": [
                {
                    "recommendationID": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "???",
                    "description": "Run a daycare",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                },
                {
                    "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "what is this for?",
                    "description": "Performs TDD",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.1"
                }
            ]
        }
    ]
}

match_table_selections = {
    "matchTable": [
        {
            "substatementID": "1fa85f64-5717-4562-b3fc-2c963f66afa6",
            "substatement": "Can perform test driven development",
            "selection": 
                {
                    "recommendationID": "2fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "what is this for?",
                    "description": "Performs TDD",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                }
        },
        {
            "substatementID": "4fa85f64-5717-4562-b3fc-2c963f66afa5",
            "substatement": "Can perform test driven development",
            "selection": 
                {
                    "recommendationID": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "name": "???",
                    "description": "Run a daycare",
                    "definedTermSet": "Standard Occupational Classification system",
                    "termCode": "19-1131.00",
                    "value": "0.9"
                }
        }
    ]
}


@describe('pipeline model')
def _():

    DB = get_db()
    DB.session.expire_on_commit = False

    my_pipeline = Pipeline(
        user_token=uuid.uuid4(),
        file_name="file_name",
        file_format="file_format",
        file_text="file_text"
    )

    DB.session.add(my_pipeline)
    DB.session.commit()

    my_pipeline_id = my_pipeline.pipeline_id
    
    @it('Pipeline.user_is_authorized_to_access_pipeline', skip=True)
    def _():
        pass

    @describe('when dealing with /match-table')
    def _():
        
        @it('can add match_table_data as json')
        def _():
            my_pipeline.match_table_data = match_table_dict
            DB.session.commit()

            expect(isinstance(my_pipeline.match_table_data, dict)).to(be_true)

        @it('can add match_table_selection as json')
        def _():
            my_pipeline.match_table_selections = match_table_selections
            DB.session.commit()
            
            expect(isinstance(my_pipeline.match_table_selections, dict)).to(be_true)

    @it('pipeline can recieve frameworks')
    def _():
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

        competency_framework = Framework(
            framework_type=competency_framework_type,
            framework_name="name4",
            framework_description="description",
            framework_uri="uri.com",
        )

        occupation_framework = Framework(
            framework_type=occupation_framework_type,
            framework_name="name5",
            framework_description="description",
            framework_uri="uri.com",
        )

        industry_framework = Framework(
            framework_type=industry_framework_type,
            framework_name="name6",
            framework_description="description",
            framework_uri="uri.com",
        )

        DB.session.add_all([
            competency_framework,
            occupation_framework,
            industry_framework
        ])

        DB.session.commit()

        nonlocal my_pipeline
        nonlocal my_pipeline_id
        DB.session.add(my_pipeline)
        my_pipeline = DB.session.query(Pipeline).filter_by(pipeline_id=my_pipeline_id).one()
                
        my_pipeline.frameworks.append(competency_framework)
        my_pipeline.frameworks.append(occupation_framework)
        my_pipeline.frameworks.append(industry_framework)

        framework_count = len(my_pipeline.frameworks)
        expect(framework_count).to(equal(3))

        expect(my_pipeline.frameworks[0].framework_id).to(equal(competency_framework.framework_id))
        expect(my_pipeline.frameworks[1].framework_id).to(equal(occupation_framework.framework_id))
        expect(my_pipeline.frameworks[2].framework_id).to(equal(industry_framework.framework_id))


