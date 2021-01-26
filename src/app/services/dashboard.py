# -*- coding: utf-8 -*-
from src.app.utils.db import mongodb_connect
from src.app.utils.redis import connection
from src.app.utils.logger import get_logger
import src.app.services.MetaModelInterpreter as MetaModelInterpreter
from simple_settings import settings


#Microservice Entrypoint
def handle_metamodel_request(message):
  logger = get_logger(__name__)
  logger.info(message.value())
  MetaModelInterpreter.Meta_Model_Interpreter(message.value())


