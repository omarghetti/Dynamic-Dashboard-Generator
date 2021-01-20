from src.app.models.base_models import *
from src.app.models.grafana_dashboard import grafana_dashboard
from src.app.models.DashboardStyle import DashboardStyle
from src.app.services.styleHandler import check_dashboard_visualization_style
import os
from src.app.utils.logger import get_logger
import json

logger = get_logger(__name__)


def Meta_Model_Interpreter(message):
  meta_model = json.load(message)

  model_uid = 'null'
  model_id = 'null'
  model_title ='example_dash'
  dashboard_style = 'null'


  for meta_model_key, meta_model_value in meta_model.items():
    if(meta_model_key == "_id"):
      model_uid = meta_model_value
    elif(meta_model_key == "dashboardpages"):
      dashboard_style = check_dashboard_visualization_style(meta_model_value)
  concrete_dashboard = grafana_dashboard(model_title, model_uid, model_id)
  style_mapping = DashboardStyle(model_uid, dashboard_style)
  logger.debug("Meta Model Interpreted ")
  logger.debug(concrete_dashboard)
  logger.debug("Style Recognized!")
  logger.debug(style_mapping)
  return concrete_dashboard, style_mapping




