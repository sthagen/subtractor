# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import Generator

import pytest  # type: ignore

from subtractor.stream import visit

TWO_FILES_FOLDER = pathlib.Path("tests", "fixtures", "two_files")
EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, "empty.png")
ANOTHER_EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, "another_empty.png")
TWO_FILES_SET = set([ANOTHER_EMPTY_PNG, EMPTY_PNG])


def test_visit_ok_test_single_fixture_file():
    empty_png = pathlib.Path("tests", "fixtures", "single_file", "empty.png")
    visitor = visit(empty_png)
    assert isinstance(visitor, Generator)
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_single_file():
    single_file_folder = pathlib.Path("tests", "fixtures", "single_file")
    empty_png = pathlib.Path(single_file_folder, "empty.png")
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
