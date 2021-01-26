from src.app.models.base_models import *
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.services.styleHandler import check_dashboard_visualization_style, create_dashboards
import os
from src.app.utils.logger import get_logger
import json

logger = get_logger(__name__)


def Meta_Model_Interpreter(message):
  meta_model = json.load(message)

  dashboard_style = 'null'
  model_uid = 'null'
  dashboards = []

  for meta_model_key, meta_model_value in meta_model.items():
    if meta_model_key == "_id":
      model_uid = meta_model_value
    elif meta_model_key == "dashboardpages":
      dashboard_style = check_dashboard_visualization_style(meta_model_value)
      dashboards = create_dashboards(meta_model_value, dashboard_style, model_uid)
  logger.debug("Meta Model Interpreted ")
  logger.debug("Style Recognized!")
  logger.debug(dashboard_style)
  logger.debug("Panels Created")
  logger.degub("Final Dashboards Ready")
  return dashboards




