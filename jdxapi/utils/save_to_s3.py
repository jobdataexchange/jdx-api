import boto3
import os
import logging
from jdxapi.s3_config import ACCESS_KEY, SECRET_KEY, JDX_PRODUCTION_OUTPUT_BUCKET
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask import request


def _upload_to_aws(local_file_path, bucket, s3_file):
    s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )
    logger = logging.getLogger('inputoutput')
    user_metadata = f'IP: {request.remote_addr} - User Agent: {request.user_agent} - URL: {request.url}'
    
    # logger.info(f'file: {local_file_path}. remote: {s3_file}')
    try:
        s3.upload_file(local_file_path, bucket, s3_file)
        logger.info(f'{user_metadata} - Upload file {local_file_path} to S3 successful.')
    except FileNotFoundError:
        logger.error(f'{user_metadata} - File {local_file_path} was not found.')
    except (NoCredentialsError, PartialCredentialsError):
        logger.error(f'{user_metadata} - Failed to upload to S3; Credentials not available or not found.')


def _folder_builder(folder, file_path):
    return f'{folder}/{file_path}'


def _upload_to_jdx_s3_folder(local_file_path, folder_path):
    OUTPUT_BUCKET = JDX_PRODUCTION_OUTPUT_BUCKET
    local_file_name = local_file_path.split('/')[-1]
    s3_file_path = _folder_builder(folder_path, local_file_name)
    _upload_to_aws(local_file_path, OUTPUT_BUCKET, s3_file_path)


def upload_jsp(local_file_path):
    JOB_SCHEMA_PLUS_FOLDER = 'job-schema-plus'
    _upload_to_jdx_s3_folder(local_file_path, JOB_SCHEMA_PLUS_FOLDER)


def upload_jsphr(local_file_path):
    JSPHER_FOLDER = 'jspher'
    _upload_to_jdx_s3_folder(local_file_path, JSPHER_FOLDER)


def upload_human_readable(local_file_path):
    JDX_HUMAN_READABLE_FOLDER = 'jdx-human-readable'
    _upload_to_jdx_s3_folder(local_file_path, JDX_HUMAN_READABLE_FOLDER)


def upload_logs(local_file_path):
    LOG_FOLDER = 'logs'
    _upload_to_jdx_s3_folder(local_file_path, LOG_FOLDER)
