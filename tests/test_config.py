""" Unit tests for configuration  """
import os
import shutil
from pathlib import Path
from pocha import describe, it, before, after
from expects import expect, equal, be_none, be_above
import importlib

# TODO we should be testing that when given a different
# env file it loads it correctly.


@describe('Config', skip=True)
def config_tests():
    """ Configuration tests.
    Unit tests for configuration
    """
    @it('Should load an environment variable', skip=True)
    def _():
        test_value = os.getenv('DEVELOPMENT')

        expect(test_value).to(equal('True'))
