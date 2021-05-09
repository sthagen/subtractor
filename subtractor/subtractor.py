# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Do the diff."""
import configparser
import csv
import json
import logging
import pathlib
import sys

from pixelmatch import pixelmatch

from subtractor.stream import visit


ENCODING = "utf-8"

APP = "subtractor"

LOG = logging.getLogger()  # Temporary refactoring: module level logger
LOG_FOLDER = pathlib.Path("logs")
LOG_FILE = f"{APP}.log"
LOG_PATH = (
    pathlib.Path(LOG_FOLDER, LOG_FILE)
    if LOG_FOLDER.is_dir()
    else pathlib.Path(LOG_FILE)
)
LOG_LEVEL = logging.INFO

FAILURE_PATH_REASON = "Failed action for path %s with error: %s"


def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global LOG  # pylint: disable=global-statement

    log_format = {
        "format": "%(asctime)s.%(msecs)03d %(levelname)s [%(name)s]: %(message)s",
        "datefmt": "%Y-%m-%dT%H:%M:%S",
        # 'filename': LOG_PATH,
        "level": LOG_LEVEL if level is None else level,
    }
    logging.basicConfig(**log_format)
    LOG = logging.getLogger(APP if name is None else name)
    LOG.propagate = True

def slugify(error):
    """Replace newlines by space."""
    return str(error).replace("\n", "")


def process(path, handler, success, failure):
    """Generic processing of path yields a,ended COHDA protocol."""
    valid, message = handler(path)
    if valid:
        return True, message, success + 1, failure

    return False, message, success, failure + 1


def main(argv=None, abort=False, debug=None):
    """Drive the subtractor.
    This function acts as the command line interface backend.
    There is some duplication to support testability.
    """
    init_logger(level=logging.DEBUG if debug else None)
    forest = argv if argv else sys.argv[1:]
    if not forest:
        print("Usage: subtractor past future")
        return 0, "USAGE"
    num_trees = len(forest)
    LOG.debug("Guarded dispatch forest=%s, num_trees=%d", forest, num_trees)

    LOG.info(
        "Starting comparisons visiting a forest with %d tree%s",
        num_trees,
        "" if num_trees == 1 else "s",
    )
    failures = 0
    for tree in forest:
        for path in visit(tree):
            if not path.is_file():
                continue

            final_suffix = "" if not path.suffixes else path.suffixes[-1].lower()

            if final_suffix == ".png":
                LOG.info("Found %s", path)

    print(f"{'OK' if not failures else 'FAIL'}")

    return 0, ""
