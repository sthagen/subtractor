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
OBS_CHILD_RGB_RED_PNG = pathlib.Path(OBS_CHILD_FOLDER, RGB_RED_NAME)


def test_main_ok_no_args(capsys):
    assert cli.main([], debug=False) == 0
    out, err = capsys.readouterr()
    assert "usage" in out.lower()
    assert not err


def test_main_nok_invalid_diff_tempalte(capsys):
    with pytest.raises(SystemExit, match="2"):
        assert cli.main([], debug=False, diff_template="invalid")
    out, err = capsys.readouterr()
    assert "error: when using external diff tool, template requires mention of $ref and $obs" in out.lower()
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
    assert "usage: subtractor past future [present]" in out.lower()
    assert not err


def test_main_nok_test_fixtures_single_png_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF_CHILD_RGB_RED_PNG], debug=False) == 0
    out, err = capsys.readouterr()
    assert "usage: subtractor past future [present]" in out.lower()
    assert not err
    lines = caplog.text.lower().split("\n")
    expected_log_line_count = 1
    assert len(lines) == expected_log_line_count
    assert not lines[0].strip()


def test_main_ok_test_fixtures_matching_png_files(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF_CHILD_RGB_RED_PNG, OBS_CHILD_RGB_RED_PNG], debug=False) == 0
    out, err = capsys.readouterr()
    assert "ok" == out.lower().strip()
    assert not err
    lines = caplog.text.lower().split("\n")
    expected_log_line_count = 10
    assert len(lines) == expected_log_line_count
    assert "starting comparisons visiting past" in lines[0].lower()
    assert "file mode" in lines[0].lower()
    assert "threshold for pixel mismatch is 1 %" in lines[1].lower()
    assert "pair" in lines[2].lower()
    for ndx in (3, 5):
        assert "to be ok with size 277 bytes" in lines[ndx].lower()
    for ndx in (4, 6):
        assert "as png to be ok with shape 2x2" in lines[ndx].lower()
    assert f"match of obs={str(OBS_CHILD_RGB_RED_PNG)}" in lines[7].lower()
    assert "finished comparisons finding good=1 and bad=0 in file mode" in lines[8].lower()
    assert not lines[9].strip()

