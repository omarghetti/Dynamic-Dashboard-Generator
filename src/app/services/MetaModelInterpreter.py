from src.app.models.base_models import *
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.services.styleHandler import check_dashboard_visualization_style
import os
from src.app.utils.logger import get_logger
import json

logger = get_logger(__name__)


def Meta_Model_Interpreter(message):
  meta_model = json.load(message)

  model_uid = 'null'


  for meta_model_key, meta_model_value in meta_model.items():
    if meta_model_key == "_id":
      model_uid = meta_model_value
    elif meta_model_key == "dashboardpages":
      Meta_Dashboard = create_meta_dashboard(meta_model_value, model_uid)
  logger.debug("Meta Model Interpreted ")
  logger.debug("Style Recognized!")
  logger.debug(Meta_Dashboard)
  return Meta_Dashboard



def create_meta_dashboard(page_list, model_uid):
  dashboard_style = check_dashboard_visualization_style(page_list)
  meta_dashboard = Meta_Dashboard(model_uid, dashboard_style)
  return meta_dashboard






