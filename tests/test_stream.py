# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import Generator

import pytest  # type: ignore

from subtractor.stream import visit


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
    two_files_folder = pathlib.Path("tests", "fixtures", "two_files")
    empty_png = pathlib.Path(two_files_folder, "empty.png")
    another_empty_png = pathlib.Path(two_files_folder, "another_empty.png")
    visitor = visit(two_files_folder)
    assert isinstance(visitor, Generator)
    first = next(visitor)
    assert first in (another_empty_png, empty_png)
    last = next(visitor)
    assert last != first and last in (another_empty_png, empty_png)
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_ok_test_fixture_folder_with_two_files():
    two_files_folder = pathlib.Path("tests", "fixtures", "two_files")
    empty_png = pathlib.Path(two_files_folder, "empty.png")
    another_empty_png = pathlib.Path(two_files_folder, "another_empty.png")
    visitor = visit(two_files_folder, a_filter=sorted)
    assert isinstance(visitor, Generator)
    assert next(visitor) == another_empty_png
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)
