# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import gennex
import hoverpower
import pytest

import pictura

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = pictura.PROCESS

hoverpower.setup(pictura.ROOT)

RESOURCES = [
    hoverpower.MASTER063_PDF,
    hoverpower.HOME043_PDF,
]


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    hoverpower.run()


def extract(resources):
    gennex.extract(
        files=resources,
        dest=hoverpower.generated(),
        rawmaker='--images',
        oneline=None,
        pdfinfo=False,
        pages='0',
    )
