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

REF_OBS_ROOT = pathlib.Path(FIXTURE_ROOT, "ref_obs")
REF_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, "ref")
OBS_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, "obs")
RGB_RED_NAME = "ff0000_2x2.png"
REF_CHILD_RGB_RED_PNG = pathlib.Path(REF_CHILD_FOLDER, RGB_RED_NAME)


def test_main_ok_no_args(capsys):
    assert cli.main([], debug=False) == 0
    out, err = capsys.readouterr()
    assert "usage" in out.lower()
    assert not err


def test_main_nok_non_existing_file(capsys):
    file_not_there = pathlib.Path("no", "file", "here")
    assert not file_not_there.exists(), f"WARNING: The path {file_not_there} SHOULD not exist, but does."
    with pytest.raises(SystemExit, match="2"):
        cli.main([str(file_not_there)], debug=False)
    out, err = capsys.readouterr()
    assert "error: for now only existing paths accepted." in out.lower()
    assert not err


def test_main_nok_test_fixtures_single_non_png_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([SINGLE_FILE_FOLDER], debug=False) == 0
    out, err = capsys.readouterr()
    assert "fail" in out.lower()
    assert not err
    assert "starting comparisons visiting a forest with 1 tree" in caplog.text.lower()
    assert f"found {SINGLE_FILE_PATH_EMPTY_PNG} to be nok with size 0 bytes" in caplog.text.lower()
    assert f"analyzed {SINGLE_FILE_PATH_EMPTY_PNG} as png to be nok with formaterror: png file has invalid signature." in caplog.text.lower()


def test_main_ok_test_fixtures_single_png_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF_CHILD_RGB_RED_PNG], debug=False) == 0
    out, err = capsys.readouterr()
    assert "ok" in out.lower()
    assert not err
    lines = caplog.text.lower().split("\n")
    expected_log_line_count = 4
    assert len(lines) == expected_log_line_count and not lines[expected_log_line_count - 1]
    assert "starting comparisons visiting a forest with 1 tree" in lines[0]
    assert f"found {REF_CHILD_RGB_RED_PNG} to be ok with size 277 bytes" in lines[1]
    assert f"analyzed {REF_CHILD_RGB_RED_PNG} as png to be ok with shape 2x2" in lines[2]
