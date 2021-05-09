# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Do the diff."""
import configparser
import csv
import json
import logging
import pathlib
import sys

from subtractor.pixel import shape_of_png
from subtractor.stream import final_suffix_in, visit


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


def slugify(thing, these=('\n',), those=(' ',)) -> str:
    """Replace these (default: new lines) by those (default: space) and return string of thing."""
    if not these or not those:
        return str(thing)
    if len(these) < len(those):
        raise ValueError("slugify called with more replacement targets than sources")
    if len(those) == 1:
        that = those[0]  # HACK A DID ACK
        if len(these) == 1:
            these = these[0]
            return str(thing).replace(these, that)
        hook = str(thing)
        for this in these:
            hook = hook.replace(this, that)
        return hook
    
    hook = str(thing)
    for this, that in zip(these, those):
        hook = hook.replace(this, that)
    return hook


def file_has_content(path: pathlib.Path) -> (bool, str):
    """Simplistic handler to develop generic processing function."""
    if not path.is_file():
        return False, f"{path} is no file"
    byte_size = path.stat().st_size
    return byte_size > 0, str(byte_size)


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
    good, bad = 0, 0
    visit_options = {
        "pre_filter": sorted,
        "pre_filter_options": {"reverse": True},
        "post_filter": final_suffix_in,
        "post_filter_options": {"suffixes": (".png",)},
    }
    for tree in forest:
        for path in visit(tree, **visit_options):
            ok, size, good, bad = process(path, file_has_content, good, bad)
            LOG.info("Found %s to be %s with size %s bytes", path, "OK" if ok else "NOK", size)
            ok, width, height, info = shape_of_png(path)
            if ok:
                message = f"shape {width}x{height}"
            else:
                message = info["error"]
            LOG.info("Analyzed %s as PNG to be %s with %s", path, "OK" if ok else "NOK", message)

    print(f"{'OK' if not bad else 'FAIL'}")

    return 0, ""
