# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Create the streams."""
import pathlib


def final_suffix_in(path, suffixes=(".png",)):
    """Simple post filter on the final suffix (including the dots)."""
    if path.is_dir():
        return False
    final_suffix = "" if not path.suffixes else path.suffixes[-1].lower()
    return final_suffix in suffixes


def visit(tree_or_file_path, pre_filter=None, pre_filter_options=None, post_filter=None, post_filter_options=None):
    """Visit tree and yield the leaves optionally pre and post filtered with corresponding options."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    elif pre_filter is None:
        if post_filter_options is None:
            post_filter_options = {}
        for path in thing.rglob("*"):
            if post_filter is None:
                yield path
            else:
                if post_filter(path, **post_filter_options):
                    yield path
    else:
        if pre_filter_options is None:
            pre_filter_options = {}
        if post_filter_options is None:
            post_filter_options = {}
        for path in pre_filter(thing.rglob("*"), **pre_filter_options):
            if post_filter is None:
                yield path
            else:
                if post_filter(path, **post_filter_options):
                    yield path
