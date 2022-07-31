# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

from subtractor.pixel import diff_img, shape_of_png

FIXTURE_ROOT = pathlib.Path('test', 'fixtures')
DEFAULT_FILE_NAME = 'empty.png'
SINGLE_FILE_FOLDER = pathlib.Path(FIXTURE_ROOT, 'single_file')
SINGLE_FILE_PATH_EMPTY_PNG = pathlib.Path(SINGLE_FILE_FOLDER, DEFAULT_FILE_NAME)

REF_OBS_ROOT = pathlib.Path(FIXTURE_ROOT, 'ref_obs')
REF_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, 'ref')
OBS_CHILD_FOLDER = pathlib.Path(REF_OBS_ROOT, 'obs')
RGB_RED_NAME = 'ff0000_2x2.png'
REF_CHILD_RGB_RED_PNG = pathlib.Path(REF_CHILD_FOLDER, RGB_RED_NAME)
OBS_CHILD_RGB_RED_PNG = pathlib.Path(OBS_CHILD_FOLDER, RGB_RED_NAME)


def test_shape_of_png_ok_test_single_fixture_rgb_file():
    ok_png, width, height, info = shape_of_png(REF_CHILD_RGB_RED_PNG)
    assert ok_png is True
    assert width == 2 and height == 2
    facts = {
        'alpha': False,
        'background': (1,),
        'bitdepth': 1,
        'gamma': 0.45455,
        'greyscale': False,
        'interlace': 0,
        'palette': [(255, 0, 0), (255, 255, 255)],
        'planes': 1,
        'size': (2, 2),
    }
    assert info == facts


def test_shape_of_png_nok_test_single_fixture_non_png_file():
    ok_png, width, height, info = shape_of_png(SINGLE_FILE_PATH_EMPTY_PNG)
    assert ok_png is False
    assert width is None and height is None
    assert info['error'].lower() == 'end of png stream.'


def test_shape_of_png_nok_non_existing_file():
    file_not_there = pathlib.Path('no', 'file', 'here')
    assert not file_not_there.exists(), f'WARNING: The path {file_not_there} SHOULD not exist, but does.'
    ok_png, width, height, info = shape_of_png(file_not_there)
    assert ok_png is False
    assert width is None and height is None
    assert info['error'].lower() == f"[errno 2] no such file or directory: '{str(file_not_there).lower()}'"


def test_diff_img_ok_ref_obs_rgb_red_file():
    tmp_png = pathlib.Path('tmp_diff_same.png')
    mismatch, w_diff, h_diff = diff_img(REF_CHILD_RGB_RED_PNG, OBS_CHILD_RGB_RED_PNG, tmp_png)
    assert mismatch == 0
    assert w_diff == 2 and h_diff == 2
    assert tmp_png.exists() and tmp_png.is_file() and tmp_png.stat().st_size == 79
    ok_png, width, height, info = shape_of_png(tmp_png)
    assert ok_png is True
    assert width == 2 and height == 2
    facts = {'alpha': False, 'bitdepth': 8, 'greyscale': False, 'interlace': 0, 'planes': 3, 'size': (2, 2)}
    assert info == facts
