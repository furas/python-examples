#!/usr/bin/env python3 

# date: 2019.11.30

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG) # global level which can block levels in handlers

sh = logging.StreamHandler()
sh.setLevel(logging.INFO)  # handler level

fh = RotatingFileHandler('logging.txt')
fh.setLevel(logging.DEBUG)  # handler level

logger.addHandler(sh)
logger.addHandler(fh)

logger.info('info')
logger.debug('debug')
