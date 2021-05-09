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


def visit(tree_or_file_path, pre_filter=None, pre_filter_options=None, post_filter=None):
    """Visit tree and yield the leaves optionally filtered."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    elif pre_filter is None:
        for path in thing.rglob("*"):
            if post_filter is None:
                yield path
            else:
                if post_filter(path):
                    yield path
    else:
        if pre_filter_options is None:
            pre_filter_options = {}
        for path in pre_filter(thing.rglob("*"), **pre_filter_options):
            if post_filter is None:
                yield path
            else:
                if post_filter(path):
                    yield path
