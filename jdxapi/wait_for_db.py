import psycopg2

# TODO pull from env
dbname = 'jdx_reference_backend_application'
user = 'postgres'
host = 'jdx-postgres'
password = 'password'

try:
    db = psycopg2.connect(
        f"dbname={dbname} user={user} host={host} password={password}"
    )
    print("Established connection with database!")

except BaseException:
    exit(1)
exit(0)

# import jdxapi.config
# import os
# from urllib.parse import urlparse
# database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')
# result = urlparse(database_uri)
# print(result.port)
# user = result.username
# password = result.password
# dbname = result.path[1:]
# host = result.hostname
# port = result.port

# while(True):
#     try:
#         connection_string = f"dbname={dbname} user={user} host={host} password={password} port={port}"
#         print(connection_string)
#         db = psycopg2.connect(
#             connection_string
#         )
#         print("Established connection with database!")
#         break

#     except BaseException:
#         print('waiting for db...')
#         raise
