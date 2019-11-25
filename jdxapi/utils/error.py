from flask import jsonify
import logging


class ApiError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload or ()

    def get_response(self):
        print(self.payload)
        logger = logging.getLogger('inputoutput')
        logger.exception('ApiError:')
        ret = dict(self.payload)
        ret['message'] = self.message
        return jsonify(ret), self.status_code # todo improve this so i can log the api resp
