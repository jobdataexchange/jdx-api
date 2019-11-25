import docker

# look for running jdx-postgres-testdb
docker_client = docker.from_env()
test_database_name = 'jdx-postgres'

def check_for_running_jdx_test_database():
    running_containers = docker_client.containers.list()
    for container in running_containers:
        if container.name == test_database_name:
            print(f'Found running test databse "{test_database_name}"')
            return True

    return False

# docker_client.containers.get('jdx-postgres')
if check_for_running_jdx_test_database() is False:

    # SPIN UP NEW DB
    print('Spinning up database in docker...')
    docker_db = docker_client.containers.run(
        "postgres:10.4-alpine",
        name='jdx-postgres',
        ports={5432: 5433},
        environment={
            'POSTGRES_USER': 'postgres',
            'POSTGRES_PASSWORD': 'password',
            'POSTGRES_DB': 'jdx_reference_backend_application'
        },
        auto_remove=True,
        detach=True
    )

    print('Docker database spinning up...')


# On exit close docker

# def close_docker_database():
#     print('Killing docker database...')
#     docker_db.stop()
#     print('Killed.')

# import atexit
# atexit.register(close_docker_database)
# print('Registered docker to close on exit...')



# wait for db
import psycopg2

import jdxapi.config
import os
from urllib.parse import urlparse
database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
result = urlparse(database_uri)
user = result.username
password = result.password
dbname = result.path[1:]
host = result.hostname
port = result.port

from time import sleep

while(True):
    try:
        connection_string = f"dbname={dbname} user={user} host={host} password={password} port={port}"
        # print(connection_string)
        db = psycopg2.connect(
            connection_string
        )
        print("Established connection with database!")
        break

    except Exception as e:
        print('waiting for db... will try again but got the following error:')
        print(type(e))
        print(str(e))
        sleep(1)





# SPIN UP TEST CLIENT
from webtest import TestApp
from jdxapi.app import app, DB

application = TestApp(app)



# Former this was used as;
# In the testing file,
# from ...pocha_setup import setup_environment, restore_environment, get_application
# setup_environment = before(setup_environment)
# restore_environment = after(restore_environment)
#
# In pocha_setup
# def setup_environment():
#     global application
#     application = TestApp(app)
#
# def restore_environment():
#     global application
#     application = None
#
# # Basic singleton
# application = TestApp(app)
#
# def get_application():
#     global application
#     return application
