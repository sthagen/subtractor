# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import Generator

import pytest  # type: ignore

from subtractor.stream import final_suffix_in, visit

FIXTURE_ROOT = pathlib.Path('test', 'fixtures')
DEFAULT_FILE_NAME = 'empty.png'
SINGLE_FILE_FOLDER = pathlib.Path(FIXTURE_ROOT, 'single_file')
SINGLE_FILE_PATH_EMPTY_PNG = pathlib.Path(SINGLE_FILE_FOLDER, DEFAULT_FILE_NAME)
TWO_FILES_FOLDER = pathlib.Path(FIXTURE_ROOT, 'two_files')
TWO_FILES_EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, DEFAULT_FILE_NAME)
TWO_FILES_ANOTHER_EMPTY_PNG = pathlib.Path(TWO_FILES_FOLDER, 'another_empty.png')
TWO_FILES_SET = {TWO_FILES_ANOTHER_EMPTY_PNG, TWO_FILES_EMPTY_PNG}

TWIN_TREE_FOLDER = pathlib.Path(FIXTURE_ROOT, 'twin_tree')
TWIN_TREE_WUN_FOLDER = pathlib.Path(TWIN_TREE_FOLDER, 'wun')
TWIN_TREE_TWO_FOLDER = pathlib.Path(TWIN_TREE_FOLDER, 'two')
TWIN_TREE_FILES_WUN_EMPTY_PNG = pathlib.Path(TWIN_TREE_WUN_FOLDER, DEFAULT_FILE_NAME)
TWIN_TREE_FILES_TWO_EMPTY_PNG = pathlib.Path(TWIN_TREE_TWO_FOLDER, DEFAULT_FILE_NAME)
TWIN_TREE_PATHS_SET = {
    TWIN_TREE_TWO_FOLDER,
    TWIN_TREE_FILES_TWO_EMPTY_PNG,
    TWIN_TREE_WUN_FOLDER,
    TWIN_TREE_FILES_WUN_EMPTY_PNG,
}


def test_visit_ok_test_single_fixture_file():
    visitor = visit(SINGLE_FILE_PATH_EMPTY_PNG)
    assert isinstance(visitor, Generator)
    assert next(visitor) == SINGLE_FILE_PATH_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_single_file():
    visitor = visit(SINGLE_FILE_FOLDER)
    assert isinstance(visitor, Generator)
    assert next(visitor) == SINGLE_FILE_PATH_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER)
    assert isinstance(visitor, Generator)
    first = next(visitor)
    assert first in TWO_FILES_SET
    last = next(visitor)
    assert last != first and last in TWO_FILES_SET
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER, pre_filter=sorted)
    assert isinstance(visitor, Generator)
    assert next(visitor) == TWO_FILES_ANOTHER_EMPTY_PNG
    assert next(visitor) == TWO_FILES_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_reverse_ok_test_fixture_folder_with_two_files():
    visitor = visit(TWO_FILES_FOLDER, pre_filter=sorted, pre_filter_options=dict(reverse=True))
    assert isinstance(visitor, Generator)
    assert next(visitor) == TWO_FILES_EMPTY_PNG
    assert next(visitor) == TWO_FILES_ANOTHER_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_twin_tree_folder_with_single_identical_files():
    visitor = visit(TWIN_TREE_FOLDER)
    assert isinstance(visitor, Generator)
    first = next(visitor)
    assert first in TWIN_TREE_PATHS_SET
    so_far = [first]
    second = next(visitor)
    assert second not in so_far and second in TWIN_TREE_PATHS_SET
    so_far.append(second)
    third = next(visitor)
    assert third not in so_far and third in TWIN_TREE_PATHS_SET
    so_far.append(third)
    last = next(visitor)
    assert last not in so_far and last in TWIN_TREE_PATHS_SET
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_filter_png_ok_test_fixture_twin_tree_folder_with_single_identical_files():
    visitor = visit(TWIN_TREE_FOLDER, post_filter=final_suffix_in)
    assert isinstance(visitor, Generator)
    first = next(visitor)
    assert first in TWIN_TREE_PATHS_SET
    so_far = [first]
    second = next(visitor)
    assert second not in so_far and second in TWIN_TREE_PATHS_SET
    so_far.append(second)
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_sorted_reverse_filter_ok_test_fixture_twin_tree_folder_with_single_identical_files():
    visit_options = {
        'pre_filter': sorted,
        'pre_filter_options': {'reverse': True},
        'post_filter': final_suffix_in,
        'post_filter_options': {'suffixes': ('.png',)},
    }
    visitor = visit(TWIN_TREE_FOLDER, **visit_options)
    assert isinstance(visitor, Generator)
    assert next(visitor) == TWIN_TREE_FILES_WUN_EMPTY_PNG
    assert next(visitor) == TWIN_TREE_FILES_TWO_EMPTY_PNG
    with pytest.raises(StopIteration):
        next(visitor)
