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

FILES = 'simple'.split()


class Lookup:

    def __init__(self):
        self.data = dict()

    def __call__(self, hashvalue):
        self.load_data()
        try:
            return self.data[hashvalue]
        except KeyError:
            utila.error(f'unknown image: {hashvalue}')
        return None

    def load_data(self):
        if self.data:
            return
        for filename in FILES:
            self.load_filename(filename)

    def load_filename(self, filename):
        root = os.path.split(__file__)[0]
        path = os.path.join(root, filename)
        if not os.path.exists(path):
            utila.error(f'missing file: {path}')
            return
        loaded = utila.file_read(path)
        for line in loaded.splitlines():
            typ, hashed, content, _ = line.split(',', maxsplit=3)
            typ = convert(typ)
            hashed = int(hashed)
            content = content.replace('[[NL]]', '\n')
            content = content.upper()
            self.data[hashed] = (typ, content)


def convert(typ):
    if 'LT' in typ:
        return picture.ImageType.LOGO | picture.ImageType.TEXT
    if 'L' in typ:
        return picture.ImageType.LOGO
    utila.error(f'unknown type: {typ}')
    return picture.ImageType.UNDEFINED


LOOKUP = Lookup()
