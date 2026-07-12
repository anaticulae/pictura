# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import hoverpower
import pytest
import utilo
import utilotest

import pictura


@utilotest.requires(hoverpower.MASTER063_PDF)
def test_image_content():
    sources = os.path.join(
        hoverpower.link(hoverpower.MASTER063_PDF),
        'rawmaker__images_images',
    )
    images = utilo.file_list(sources, exclude='yaml', absolute=True)
    first = images[0]
    loaded = pictura.imageload(first)
    detected = pictura.detect(loaded)
    assert detected.detected == pictura.LOGO_TEXT
    # TODO: ENABLE LATER
    expected = 'IN DEI NOMINE FELICITER\nRADBOUD UNIVERSITEIT NIJMEGEN'
    assert detected.text == expected


EXPECTED = """\
DHBW
DUALE HOCHSCHULE
BADEN WUERTEMBERG
""".strip()


@pytest.mark.xfail(reason='software integration')
@utilotest.requires(hoverpower.HOME043_PDF)
def test_text_frompath():
    sources = os.path.join(
        hoverpower.link(hoverpower.HOME043_PDF),
        'rawmaker__images_images',
    )
    images = utilo.file_list(sources, exclude='yaml', absolute=True)
    first = images[0]
    text = pictura.text_frompath(first)
    assert text == EXPECTED
