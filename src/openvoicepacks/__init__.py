"""
.. include:: ../../README.md
   :start-line: 2
"""

import logging
import os

import coloredlogs

from openvoicepacks.client import *

# Load settings from environment variables
_environment = os.environ.get("OVP_ENVIRONMENT", "development")
_loglevel = os.environ.get("OVP_LOG_LEVEL", "DEBUG").upper()

# Remove any default handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Install coloredlogs on the root logger
_LOGFORMAT = "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
coloredlogs.install(level=_loglevel, fmt=_LOGFORMAT)
