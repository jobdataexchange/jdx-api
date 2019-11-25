import functools
import logging
from flask_restful import Resource
from flask import request
import json

def failsafe_pp_json_obj(json_obj):
    try:
        return json.dumps(json_obj, indent=4)
    except:
        return json_obj


def log_input_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger('inputoutput')
        # print(dir(request.))
        user_metadata = f'IP: {request.remote_addr} - User Agent: {request.user_agent} - URL: {request.url}'
        logger.info(f'{user_metadata} - Request Body: {failsafe_pp_json_obj(request.get_json())}')
        # logger.info(failsafe_pp_json_obj(request.get_json()))

        output = func(*args, **kwargs)
    
        logger.info(f'{user_metadata} - Response Body: {failsafe_pp_json_obj(output.get_json())}')
        
        return output
        # restful.abort(401)
    return wrapper


class LoggerResource(Resource):
    method_decorators = [log_input_output]   
