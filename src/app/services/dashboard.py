# -*- coding: utf-8 -*-
from utils.redis import connection
from utils.logger import get_logger

def handle_monitoring_request(message):
  logger = get_logger(__name__)
  logger.info(message.value())
