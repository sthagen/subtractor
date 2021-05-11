# -*- coding: utf-8 -*-
# pylint: disable=c-extension-no-member,expression-not-assigned,line-too-long,logging-fstring-interpolation
"""Juggle with pixels."""
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import png

OPTIONS = {"threshold": 0.05}


def shape_of_png(path):
    """MVP like initial shape reader for PNG from path."""
    try:
        with path.open("rb") as handle:
            a_png = png.Reader(file=handle)
            width, height, _, info = a_png.read()  # Ignore the rows iterator
            return True, width, height, info
    except Exception as err:  # pylint: disable=broad-except
        return False, None, None, {"error": str(err).replace("\n", "$NL$")}


def read_img(path):
    """HACK A DID ACK"""
    return Image.open(path)


def pil_to_flatten_data(img):
    """
    Convert data from [(R1, G1, B1, A1), (R2, G2, B2, A2)] to [R1, G1, B1, A1, R2, G2, B2, A2]
    """
    return [x for p in img.convert("RGBA").getdata() for x in p]


def diff_img(ref, obs, sub):
    """Read from ref and obs, calculate the subtraction, output at sub.

    Returns the mismatch pixel count, width, and height."""
    img_a = read_img(ref)
    img_b = read_img(obs)
    width, height = img_a.size
    img_diff = Image.new("RGB", (width, height))
    mismatch = pixelmatch(img_a, img_b, img_diff, **OPTIONS)

    img_diff.save(sub)
    return mismatch, width, height
