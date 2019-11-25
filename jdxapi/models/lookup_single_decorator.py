import functools
from jdxapi.utils.error import ApiError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def lookup_single_error_handler(value_name):
    print(f'name {value_name}')
    def real_decorator(fn):
        @functools.wraps(fn)
        def wrapped_fn(*args, **kwargs):
            try:
                output = fn(*args, **kwargs)

            except MultipleResultsFound:
                raise ApiError(f"Multiple results found for '{value_name}' but was expecting one result.", 500)

            except NoResultFound:
                raise ApiError(f"'{value_name}' not found.", 404)

            return output

        return wrapped_fn
    
    return real_decorator
