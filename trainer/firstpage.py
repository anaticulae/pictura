# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Collect first pages, extract logo and determine content by hand."""

import os

import hoverpower
import utilo

import pictura

ROOT = utilo.tmpdir(pictura.ROOT)


def extractpdf(pdf):
    filename = utilo.simple(os.path.split(pdf)[1])
    path = os.path.join(ROOT, filename)
    os.makedirs(path)
    cmd = f'rawmaker -i {pdf} -o {path} --images --pages=0,1,2'
    utilo.debug(cmd)
    utilo.run(cmd)
    return path


def imageinfo(path: str):
    document = os.path.split(path)[1]
    sources = os.path.join(path, 'rawmaker__images_images')
    if not os.path.exists(sources):
        utilo.debug(f'path does not exists: {sources}')
        return
    images = utilo.file_list(sources, exclude='yaml', absolute=True)
    for image in images:
        loaded = pictura.imageload(image)
        hashed = pictura.imagehash(loaded)
        utilo.log(',', end='')
        utilo.log(hashed, end=',')
        utilo.log('', end=',')
        utilo.log(document, end=' ')
        utilo.log(image)


if __name__ == "__main__":
    for filepath in hoverpower.PDF:
        extacted = extractpdf(filepath)
        imageinfo(extacted)
