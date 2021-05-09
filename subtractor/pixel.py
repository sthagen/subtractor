# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Juggle with pixels."""
import pathlib

from pixelmatch import pixelmatch
import png


def shape_of_png(path):
    """MVP like initial shape reader for PNG from path."""
    try:
        with path.open("rb") as handle:
            a_png = png.Reader(file=handle)
            width, height, rows, info = a_png.read()
            return True, f"shape {width}x{height}"
    except Exception as err:  # pylint: disable=too-broad-exception
        return False, str(err).replace("\n", "$NL$")
