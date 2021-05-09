# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import Generator

import pytest  # type: ignore

from subtractor.stream import visit

FIXTURE_ROOT = pathlib.Path("tests", "fixtures")
DEFAULT_FILE_NAME = "empty.png"
SINGLE_FILE_FOLDER = pathlib.Path(FIXTURE_ROOT, "single_file")
TWO_FILES_FOLDER = pathlib.Path(FIXTURE_ROOT, "two_files")
EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, DEFAULT_FILE_NAME)
ANOTHER_EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, "another_empty.png")
TWO_FILES_SET = {ANOTHER_EMPTY_PNG, EMPTY_PNG}


def test_visit_ok_test_single_fixture_file():
    empty_png = pathlib.Path(SINGLE_FILE_FOLDER, DEFAULT_FILE_NAME)
    visitor = visit(empty_png)
    assert isinstance(visitor, Generator)
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_single_file():
    single_file_folder = pathlib.Path(SINGLE_FILE_FOLDER)
    empty_png = pathlib.Path(single_file_folder, DEFAULT_FILE_NAME)
    visitor = visit(single_file_folder)
    assert isinstance(visitor, Generator)
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER)
    assert isinstance(visitor, Generator)
    first = next(visitor)
    assert first in (ANOTHER_EMPTY_PNG, EMPTY_PNG)
    last = next(visitor)
    assert last != first and last in TWO_FILES_SET
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER, a_filter=sorted)
    assert isinstance(visitor, Generator)
    assert next(visitor) == ANOTHER_EMPTY_PNG
    assert next(visitor) == EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_reverse_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER, a_filter=sorted, filter_options=dict(reverse=True))
    assert isinstance(visitor, Generator)
    assert next(visitor) == EMPTY_PNG
    assert next(visitor) == ANOTHER_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)
