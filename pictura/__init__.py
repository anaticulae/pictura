#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import importlib.metadata
import os

from pictura.data import LOGO_TEXT
from pictura.data import ImageContent
from pictura.data import ImageType
from pictura.detector import detect
from pictura.detector import text_frompath
from pictura.hasher import imagehash
from pictura.hasher import imageload

PROCESS = 'pictura'
__version__ = importlib.metadata.version(PROCESS)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
