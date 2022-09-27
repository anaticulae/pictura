# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power
import pytest

import picture

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = picture.PROCESS

power.setup(picture.ROOT)

RESOURCES = [
    power.MASTER063_PDF,
    power.HOME040_PDF,
]


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    genex.extract(
        files=resources,
        dest=power.generated(),
        rawmaker='--images',
        oneline=None,
        pdfinfo=False,
        pages='0',
    )
