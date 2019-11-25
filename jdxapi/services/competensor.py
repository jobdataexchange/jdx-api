from nameko.standalone.rpc import ClusterRpcProxy
from jdxapi.utils.error import ApiError
from nameko.exceptions import RemoteError, UnknownService
import functools
import logging


config = {
    'AMQP_URI': 'amqp://guest:guest@rabbitmq'
}


def competensor_error_handler(fn):
    @functools.wraps(fn)
    def wrapped_fn(*args, **kwargs):
        try:
            output = fn(*args, **kwargs)
        except ConnectionRefusedError:
            raise ApiError('Unable to communicate with Competensor.', 503)
        except OSError as e:
            if str(e) == 'failed to resolve broker hostname':
                raise ApiError('Competensor service seems to be down.', 500)
            else:
                raise ApiError('Unknown error occured with Competensor.', 500)
        except RemoteError:
            raise ApiError('Failure from Competensor.', 500)
        except UnknownService:
            raise ApiError('Competensor is either currently loading or down.', 500)
        
        except Exception as e: # TODO this should be removed from production
            error_message = f'Uncaught exception: {e}, {type(e)}, {str(e)}'
            raise ApiError(error_message)
        return output
    return wrapped_fn


@competensor_error_handler
def get_preview(pipeline_id):
    with ClusterRpcProxy(config) as cluster_rpc:
        data = cluster_rpc.previewer.preview(pipeline_id)
        return data


@competensor_error_handler
def get_framework_recommendations(pipeline_id):
    with ClusterRpcProxy(config) as cluster_rpc:
        data = cluster_rpc.frameworks.recommend(pipeline_id)
        return data


@competensor_error_handler
def get_match_table(pipeline_id, frameworks, threshold):
    with ClusterRpcProxy(config) as cluster_rpc:
        # data = cluster_rpc.competensor.get_match_table_and_jsonld(pipeline_id, "Cybersecurity-Industry", threshold)
        data = cluster_rpc.competensor.get_match_table_and_jsonld(pipeline_id, frameworks, threshold)
        return data


@competensor_error_handler
def generate_job_schema_plus(pipeline_id):
    with ClusterRpcProxy(config) as cluster_rpc:
        data = cluster_rpc.generate_schema.generate_job_schema_file(pipeline_id)
        return data


@competensor_error_handler
def health():
    with ClusterRpcProxy(config) as cluster_rpc:
        _ = cluster_rpc.greeter_service.greet("Hello from API!")
        return 200
