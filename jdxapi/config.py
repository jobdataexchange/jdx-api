""" Project related config

    This file, using dotenv, takes settings from .env file and makes
    them accessible from `os.getenv('STRING')`.
"""
import os
from dotenv import load_dotenv
from pathlib import Path

ENV_PATH = os.getenv('ENV_PATH', '.env-os-test')
load_dotenv(dotenv_path=ENV_PATH, override=True)
