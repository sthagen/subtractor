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
