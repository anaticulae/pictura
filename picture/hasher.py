# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import PIL.Image
import utila


def imagehash(image: PIL.Image.Image) -> int:
    """\
    >>> assert imagehash(PIL.Image.new('1', (512, 512), color=0))
    """
    image = image_normalize(image)
    png = image._repr_png_()  # pylint:disable=W0212
    result = utila.binhash(png)
    return result


def imageload(path: str) -> PIL.Image.Image:
    with PIL.Image.open(path) as image:
        result = image_normalize(image)
    return result


IMAGE_SIZE = (512, 512)


def image_normalize(image: PIL.Image.Image) -> PIL.Image.Image:
    resized = image.resize(IMAGE_SIZE)
    return resized
