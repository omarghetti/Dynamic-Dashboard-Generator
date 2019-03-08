# -*- coding: utf-8 -*-

import logging, sys
from simple_settings import settings

FORMATTER = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')

def configure_logger(logger):
  if not logger.hasHandlers():
    if settings.DEBUG:
      logger.setLevel(logging.DEBUG)
    else:
      logger.setLevel(loggin.INFO)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(FORMATTER)
    logger.addHandler(handler)
    logger.propagate = False
  return logger

def get_logger(logger_name):
  logger = configure_logger(logging.getLogger(logger_name))
  return logger
