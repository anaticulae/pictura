# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

import picture
import power


def test_image_content():
    sources = os.path.join(
        power.link(power.MASTER063_PDF),
        'rawmaker__images_images',
    )
    images = utila.file_list(sources, exclude='yaml', absolute=True)
    first = images[0]
    loaded = picture.imageload(first)
    detected = picture.detect(loaded)
    assert detected.detected == picture.LOGO_TEXT
    # TODO: ENABLE LATER
    expected = 'IN DEI NOMINE FELICITER\nRADBOUD UNIVERSITEIT NIJMEGEN'
    assert detected.text == expected
