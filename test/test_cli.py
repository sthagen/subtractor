# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import logging
import pathlib

import pytest  # type: ignore

import subtractor.cli as cli

ENCODING = 'utf-8'

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

REF_OBS_TWO_ROOT = pathlib.Path(FIXTURE_ROOT, 'ref_obs_two')
REF2_CHILD_FOLDER = pathlib.Path(REF_OBS_TWO_ROOT, 'ref')
OBS2_CHILD_FOLDER = pathlib.Path(REF_OBS_TWO_ROOT, 'obs')
REF2_CHILD_RGB_RED_PNG = pathlib.Path(REF2_CHILD_FOLDER, RGB_RED_NAME)
OBS2_CHILD_RGB_RED_PNG = pathlib.Path(OBS2_CHILD_FOLDER, RGB_RED_NAME)


def test_main_ok_no_args(capsys):
    assert cli.main([], debug=False) == 0
    out, err = capsys.readouterr()
    assert 'usage' in out.lower()
    assert not err


def test_main_nok_invalid_diff_template(capsys):
    with pytest.raises(SystemExit, match='2'):
        cli.main([], debug=False, diff_template='invalid')
    out, err = capsys.readouterr()
    assert 'error: when using external diff tool, template requires mention of $ref and $obs' in out.lower()
    assert not err


def test_main_nok_valid_diff_template(caplog, capsys):
    caplog.set_level(logging.INFO)
    diff_template = 'echo $ref $obs'
    assert cli.main([REF_CHILD_RGB_RED_PNG, OBS_CHILD_RGB_RED_PNG], debug=False, diff_template=diff_template) == 0
    out, err = capsys.readouterr()
    assert out.lower().strip() == 'ok'
    assert not err
    lines = caplog.text.lower().split('\n')
    expected_log_line_count = 13
    assert len(lines) == expected_log_line_count
    assert f'requested external diff tool per template({diff_template})' in lines[0].lower()
    assert f'parsed diff template ({diff_template}) into executor' in lines[1].lower()
    assert (
        f"into executor ({{'executor': '{diff_template}', 'param_file_content': none, 'param_file_name': none}}"
    ) in lines[2].lower()
    assert 'starting comparisons visiting past' in lines[3].lower()
    assert 'file mode' in lines[3].lower()
    assert 'threshold for pixel mismatch is 1 %' in lines[4].lower()
    assert 'pair' in lines[5].lower()
    for ndx in (6, 8):
        assert 'to be ok with size 277 bytes' in lines[ndx].lower()
    for ndx in (7, 9):
        assert 'as png to be ok with shape 2x2' in lines[ndx].lower()
    # assert f'{str(REF_CHILD_RGB_RED_PNG)} {str(OBS_CHILD_RGB_RED_PNG)} ' in str(lines[8]).lower()
    assert 'finished comparisons finding good=1 and bad=0 in file mode' in lines[11].lower()
    assert not lines[12].strip()


def test_main_nok_valid_diff_param_file_template(caplog, capsys):
    caplog.set_level(logging.CRITICAL)
    param_file_name = 'foo'
    content_template = 'asd=42 $ref $obs'
    expected_content = content_template.replace('$ref', str(REF_CHILD_RGB_RED_PNG)).replace(
        '$obs', str(OBS_CHILD_RGB_RED_PNG)
    )
    diff_template = f'echo $ref $obs @{param_file_name}:$file:{content_template}:$name:{param_file_name}'
    assert cli.main([REF_CHILD_RGB_RED_PNG, OBS_CHILD_RGB_RED_PNG], debug=False, diff_template=diff_template) == 0
    assert pathlib.Path(param_file_name).exists() and pathlib.Path(param_file_name).is_file()
    with open(param_file_name, 'rt', encoding=ENCODING) as handle:
        read_content = handle.read()
    assert read_content == expected_content
    out, err = capsys.readouterr()
    assert out.lower().strip() == 'ok'
    assert not err
    lines = caplog.text.lower().split('\n')
    expected_log_line_count = 1
    assert len(lines) == expected_log_line_count
    assert not lines[0].strip()


def test_main_nok_non_existing_file(capsys):
    file_not_there = pathlib.Path('no', 'file', 'here')
    assert not file_not_there.exists(), f'WARNING: The path {file_not_there} SHOULD not exist, but does.'
    with pytest.raises(SystemExit, match='2'):
        cli.main([str(file_not_there)], debug=False)
    out, err = capsys.readouterr()
    assert 'error: for now only existing paths accepted.' in out.lower()
    assert not err


def test_main_nok_test_fixtures_single_non_png_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([SINGLE_FILE_FOLDER], debug=False) == 0
    out, err = capsys.readouterr()
    assert 'usage: subtractor past future [present]' in out.lower()
    assert not err


def test_main_nok_test_fixtures_file_and_folder(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([SINGLE_FILE_PATH_EMPTY_PNG, SINGLE_FILE_FOLDER], debug=False) == 2
    out, err = capsys.readouterr()
    assert 'error: either all args are dirs or files, but no mix' in out.lower()
    assert not err


def test_main_nok_test_fixtures_folder_and_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([SINGLE_FILE_FOLDER, SINGLE_FILE_PATH_EMPTY_PNG], debug=False) == 2
    out, err = capsys.readouterr()
    assert 'error: either all args are dirs or files, but no mix' in out.lower()
    assert not err


def test_main_nok_test_fixtures_single_png_file(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF_CHILD_RGB_RED_PNG], debug=False) == 0
    out, err = capsys.readouterr()
    assert 'usage: subtractor past future [present]' in out.lower()
    assert not err
    lines = caplog.text.lower().split('\n')
    expected_log_line_count = 1
    assert len(lines) == expected_log_line_count
    assert not lines[0].strip()


def test_main_ok_test_fixtures_matching_png_files(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF_CHILD_RGB_RED_PNG, OBS_CHILD_RGB_RED_PNG], debug=False) == 0
    out, err = capsys.readouterr()
    assert out.lower().strip() == 'ok'
    assert not err
    lines = caplog.text.lower().split('\n')
    expected_log_line_count = 10
    assert len(lines) == expected_log_line_count
    assert 'starting comparisons visiting past' in lines[0].lower()
    assert 'file mode' in lines[0].lower()
    assert 'threshold for pixel mismatch is 1 %' in lines[1].lower()
    assert 'pair' in lines[2].lower()
    for ndx in (3, 5):
        assert 'to be ok with size 277 bytes' in lines[ndx].lower()
    for ndx in (4, 6):
        assert 'as png to be ok with shape 2x2' in lines[ndx].lower()
    assert f'match of obs={str(OBS_CHILD_RGB_RED_PNG)}' in lines[7].lower()
    assert 'finished comparisons finding good=1 and bad=0 in file mode' in lines[8].lower()
    assert not lines[9].strip()


def test_main_nok_folders_of_matching_png_files(caplog, capsys):
    caplog.set_level(logging.INFO)
    assert cli.main([REF2_CHILD_FOLDER, OBS2_CHILD_FOLDER], debug=False) == 0
    out, err = capsys.readouterr()
    assert out.lower().strip() == 'ok'
    assert not err
    lines = caplog.text.lower().split('\n')
    expected_log_line_count = 16
    assert len(lines) == expected_log_line_count
    assert 'starting comparisons visiting past' in lines[0].lower()
    assert 'folder mode' in lines[0].lower()
    assert 'threshold for pixel mismatch is 1 %' in lines[1].lower()
    assert 'pair' in lines[2].lower()
    for ndx in (3, 5):
        assert 'to be ok with size 277 bytes' in lines[ndx].lower()
    for ndx in (4, 6):
        assert 'as png to be ok with shape 2x2' in lines[ndx].lower()
    assert f'match of obs={str(OBS2_CHILD_RGB_RED_PNG)}' in lines[7].lower()
    assert 'finished comparisons finding good=2 and bad=0 in folder mode' in lines[14].lower()
    assert not lines[15].strip()
