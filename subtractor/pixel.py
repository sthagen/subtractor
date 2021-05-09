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
            width, height, _, info = a_png.read()  # Ignore the rows iterator
            return True, width, height, info
    except Exception as err:  # pylint: disable=too-broad-exception
        return False, None, None, {"error": str(err).replace("\n", "$NL$")}
