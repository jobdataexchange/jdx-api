This application should be run along side [competensor](https://github.com/jobdataexchange/competensor). The frontend to walk through the workflow is here, [reference-app-ui](https://github.com/jobdataexchange/reference-app-ui).

## How to use
1. Install Docker per their instructions, https://docs.docker.com/install/

2. Download this repo by using the following commands,
```bash
$ git clone https://github.com/brighthive/jdx-api.git
$ cd jdx-api
```

3. To start the server use the following command,
```bash
docker-compose up
```

4. At this point the server should spin up and will eventually report the IP address where you can access it, typically `http://0.0.0.0:8000`. You should also be able to access it at `http://localhost:8000`.

## Setting up for Development
### Mac specific
(If you are on mac and have trouble installing postgres related libraries, psycopg2, pgcli, try the following)

Step 1.

brew install openssl

Step 2.

export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/

### General instructions

As a quick overview, to set up a development environment you will need to clone the repository and setup a virtual environment with [Pipenv](https://docs.pipenv.org/).

_The following provided instructions are for ubuntu._

1. Ensure you have Python and PostgreSQL development libraries installed,
```bash
sudo apt-get install libpq-dev python-dev
```

2. Install `pipenv` by following these [instructions](https://docs.pipenv.org/en/latest/install/#installing-pipenv).

3. Clone the repo,
```bash
$ git clone https://github.com/brighthive/jdx-api.git
$ cd jdx-api
```

4. Install things for textract (This pipfile contains a fork of textract that works for this repo).

4a. Install the prereqs (https://textract.readthedocs.io/en/latest/installation.html)
```bash
apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig libpulse-dev
```
4b. Install a fake dependency for textract. (Why do I need to do this? https://github.com/deanmalmgren/textract/pull/178). Run the following command,
```
pipenv shell
curl https://raw.githubusercontent.com/OriHoch/textract/fake-pocketsphinx-for-swig-dependency/provision/fake-pocketsphinx.sh | bash -
exit
```

5. Install the Python production and development dependencies,
```bash
$ pipenv install --dev
``` 

To run tests see the running test section.

To run the application see the how to use section.

Have fun developing!

<!-- 
### Linting

To run autopep8,
```bash
$ pipenv run autopep8 --in-place --aggressive --aggressive -r ./
```
-->

### Commonly used development commands
Please see `/scripts/jdx-cli.sh` for commonly used commands.

### Running tests

To run the test suite first you must stand up a database,
```bash
$ docker-compose -f docker-compose-test.yml down && sudo docker-compose -f docker-compose-test.yml build && docker-compose -f docker-compose-test.yml up
```

Then run the tests with,
```bash
$ pipenv run pocha tests
```

# API Reference

Swagger spec / OpenAPI Specification is located at `https://app.swaggerhub.com/apis/loganripplinger/JDX-reference-backend-application-real`

<!--
## Database inspection

The database may be inspected using `pgcli`
```
pipenv pgcli
```

To connect to postgres running in docker-compose,
```
docker-compose up
docker-compose exec jdx-postgres psql -U postgres
```

In psql,
- List all databases, `\l`
- Enter database, `\c database`
- View all tables, `\d`


```bash
(ace-act-Rs3bqtfg) kwame@Puget-168695:/hdd/work/BrightHive/ACE$ pgcli postgres://postgres:password@localhost:5433/act
/home/kwame/.local/lib/python3.5/site-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
Version: 0.20.1
Chat: https://gitter.im/dbcli/pgcli
Mail: https://groups.google.com/forum/#!forum/pgcli
Home: http://pgcli.com
act> \l
+-----------+
| datname   |
|-----------|
| postgres  |
| act       |
| template1 |
| template0 |
+-----------+
SELECT 4
Time: 0.002s
act> \d
+----------+-----------------+--------+----------+
| Schema   | Name            | Type   | Owner    |
|----------+-----------------+--------+----------|
| public   | act_result      | table  | postgres |
| public   | alembic_version | table  | postgres |
| public   | context         | table  | postgres |
| public   | course          | table  | postgres |
| public   | ttl             | table  | postgres |
+----------+-----------------+--------+----------+
SELECT 5
Time: 0.005s
act> 
```
-->

## Output files
As users go through the workflow JDX API will produce a number of files.

These files along with API logs are saved within the /logs folder and subfolders.

To enable these files to be pushed to an S3 bucket edit the bucket name, access and secret keys within `jdxapi/s3_config.py`.

## Related repositories

- CLI End to end testing client
  https://github.com/jobdataexchange/jdx-e2e-client-py

- Swagger file backup
  https://github.com/jobdataexchange/jdx-api-swagger
  https://app.swaggerhub.com/apis/loganripplinger/JDX-reference-backend-application-real

- Convert internal intermediate JobSchema+ human readable to txt for dissemination
  https://github.com/jobdataexchange/jdx-internal-jsphr-converter

- OpenAPI generated python client for end to end client
  https://github.com/jobdataexchange/jdx-client-api-python
