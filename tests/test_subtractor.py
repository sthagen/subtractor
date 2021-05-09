# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pytest  # type: ignore

from subtractor.subtractor import process, slugify


def test_process_ok_test_mock_valid_handler():
    def mock_valid_message(arg):
        _ = arg
        return True, "test"

    good, bad = 42, -1
    ok, message, good, bad = process(None, mock_valid_message, good, bad)
    assert ok is True
    assert message == "test"
    assert good == 42 + 1
    assert bad == -1


def test_process_nok_test_mock_invalid_handler():
    def mock_invalid_message(arg):
        _ = arg
        return False, "test"

    good, bad = 42, -1
    ok, message, good, bad = process(None, mock_invalid_message, good, bad)
    assert ok is False
    assert message == "test"
    assert good == 42
    assert bad == 0


def test_slugify_ok_no_newline():
    assert slugify("one line") == "one line"
