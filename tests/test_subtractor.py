# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest  # type: ignore

from subtractor.subtractor import process, slugify


def test_process_ok_test_single_fixture_rgb_file():
    def mock_valid_message(arg):
        _ = arg
        return True, "test"
    good, bad = 42, -1
    ok, message, good, bad = process(None, mock_valid_message, good, bad)
    assert ok is True
    assert message == "test"
    assert good == 42 + 1
    assert bad == -1

