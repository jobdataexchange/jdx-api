from jdxapi.app import create_app
from flask_sqlalchemy import SQLAlchemy

def setup_environment():
    global app
    global testDB
#     print(app, testDB)
    with app.app_context():
        testDB.create_all()
    

def restore_environment():
    global app
    global testDB
#     print(app, testDB)
    with app.app_context():
        testDB.drop_all()
    

# Basic singleton
app = create_app()
testDB = SQLAlchemy(app)

def get_app():
    global app
    return app

def get_db():
    global testDB
    return testDB
