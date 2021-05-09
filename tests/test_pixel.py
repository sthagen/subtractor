# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import pytest  # type: ignore

from subtractor.pixel import shape_of_png

FIXTURE_ROOT = pathlib.Path("tests", "fixtures")
DEFAULT_FILE_NAME = "empty.png"
SINGLE_FILE_FOLDER = pathlib.Path(FIXTURE_ROOT, "single_file")
SINGLE_FILE_PATH_EMPTY_PNG = pathlib.Path(SINGLE_FILE_FOLDER, DEFAULT_FILE_NAME)

REF_OBS_ROOT = pathlib.Path(FIXTURE_ROOT, "ref_obs")
REF_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, "ref")
OBS_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, "obs")
RGB_RED_NAME = "ff0000_2x2.png"
REF_CHILD_RGB_RED_PNG = pathlib.Path(REF_CHILD_FOLDER, RGB_RED_NAME)


def test_visit_ok_test_single_fixture_rgb_file():
    ok, message = shape_of_png(REF_CHILD_RGB_RED_PNG)
    assert ok is True
    assert message == "shape 2x2"


def test_visit_nok_test_single_fixture_non_png_file():
    ok, message = shape_of_png(SINGLE_FILE_PATH_EMPTY_PNG)
    assert ok is False
    assert message.lower() == "formaterror: png file has invalid signature."


def test_visit_nok_non_existing_file():
    file_not_there = pathlib.Path("no", "file", "here")
    ok, message = shape_of_png(file_not_there)
    assert ok is False
    assert message.lower() == f"[errno 2] no such file or directory: '{str(file_not_there).lower()}'"
