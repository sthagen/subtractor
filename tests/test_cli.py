# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import logging
import pathlib

import pytest  # type: ignore

import subtractor.cli as cli


FIXTURE_ROOT = pathlib.Path("tests", "fixtures")
DEFAULT_FILE_NAME = "empty.png"
SINGLE_FILE_FOLDER = pathlib.Path(FIXTURE_ROOT, "single_file")
SINGLE_FILE_PATH_EMPTY_PNG = pathlib.Path(SINGLE_FILE_FOLDER, DEFAULT_FILE_NAME)


def test_main_ok_no_args(capsys):
    assert cli.main([], debug=False) == 0
    out, err = capsys.readouterr()
    assert "usage" in out.lower()
    assert not err


def test_main_ok_test_fixtures_single_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([SINGLE_FILE_FOLDER], debug=False) == 0
    out, err = capsys.readouterr()
    assert "ok" in out.lower()
    assert not err
    assert "starting comparisons visiting a forest with 1 tree" in caplog.text.lower()
    assert f"found {SINGLE_FILE_PATH_EMPTY_PNG} to be ok" in caplog.text.lower()
