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


def visit(tree_or_file_path):
    """Visit tree and yield the leaves."""
    thing = pathlib.Path(tree_or_file_path)
    if thing.is_file():
        yield thing
    else:
        for path in thing.rglob("*"):
            yield path
