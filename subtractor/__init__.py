"""Pixels, pixels, pixels."""
import os
from typing import List

APP_NAME = 'Pixels, pixels, pixels.'
APP_ALIAS = 'subtractor'
APP_ENV = 'SUBTRACTOR'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.subtractor.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.8.1+parent.402b0885'
# [[[end]]] (checksum: 5f96eaee02d1eb55e321959964bc02c7)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
