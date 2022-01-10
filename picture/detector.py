# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import PIL.Image

import picture
import picture_trained


def detect(image: PIL.Image.Image) -> picture.ImageContent:
    hashed = picture.imagehash(image)
    detected = picture_trained.LOOKUP(hashed)
    if not detected:
        return None
    text = detected[1]
    result = picture.ImageContent(detected=detected[0], text=text)
    return result
