# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib
from typing import Generator

import pytest  # type: ignore

from subtractor.stream import visit


def test_visit_ok_test_fixture_file():
    empty_png = pathlib.Path("tests", "fixtures", "empty.png")
    visitor = visit(empty_png)
    assert isinstance(visitor, Generator)
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)


def test_visit_ok_test_fixture_folder_with_wun_file():
    single_file_folder = pathlib.Path("tests", "fixtures")
    empty_png = pathlib.Path(single_file_folder, "empty.png")
    visitor = visit(single_file_folder)
    assert isinstance(visitor, Generator)
    assert next(visitor) == empty_png
    with pytest.raises(StopIteration):
        next(visitor)
