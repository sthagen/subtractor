# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Create the streams."""
import pathlib


def walk_tree_explicit(base_path):
    """Visit the files in the folders below base path."""
    if base_path.is_file():
        yield base_path
    else:
        for entry in base_path.iterdir():
            if entry.is_dir():
                for file_path in entry.iterdir():
                    yield file_path
            else:
                yield entry


def visit(tree_or_file_path, a_filter=None, filter_options=None):
    """Visit tree and yield the leaves optionally filtered."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    elif a_filter is None:
        for path in thing.rglob("*"):
            yield path
    else:
        if filter_options is None:
            filter_options = {}
        for path in a_filter(thing.rglob("*"), **filter_options):
            yield path
