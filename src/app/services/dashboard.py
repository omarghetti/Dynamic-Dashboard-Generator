# -*- coding: utf-8 -*-
from src.app.utils.db import mongodb_connect
from src.app.utils.redis import connection
from src.app.utils.logger import get_logger
from src.app.models.base_models import DashboardGlobal, DashboardItem, DashboardPage
from simple_settings import settings
import pymongo


def handle_metamodel_request(message):
  logger = get_logger(__name__)
  logger.info(message.value())
  






