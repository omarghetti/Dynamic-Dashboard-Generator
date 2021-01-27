# -*- coding: utf-8 -*-
from src.app.utils.db import mongodb_connect
from src.app.utils.redis import connection
from src.app.utils.logger import get_logger
import src.app.services.MetaModelInterpreter as MetaModelInterpreter
from simple_settings import settings
from src.app.services.Ontology_Processor import query_ontology


#Microservice Entrypoint
#From Here, we create dashboard objects and panel objects to use for querying the ontology
#to generate our dynamic dashboard
def handle_metamodel_request(message):
  logger = get_logger(__name__)
  logger.info(message.value())
  dashboards = MetaModelInterpreter.Meta_Model_Interpreter(message.value())
  ontology_matching_dashboard = query_ontology(dashboards)




