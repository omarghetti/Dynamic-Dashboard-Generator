from bson import ObjectId
from src.app.models.base_models import *
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.services.grafana_ontology_processor import query_ontology_for_grafana
from src.app.services.kibana_ontology_processor import query_ontology_for_kibana
from src.app.services.styleHandler import check_dashboard_visualization_style, \
  create_dashboards_for_grafana,create_dashboards_for_kibana
import os
from src.app.utils.logger import get_logger
import json


logger = get_logger(__name__)


def meta_model_interpreter(message):
  meta_model = json.loads(message)
  viz_tool = os.environ.get('SELECTED_TOOL')
  dashboard_style = 'null'
  model_uid = 'null'
  dashboards = []
  final_dashboards = []

  for meta_model_key, meta_model_value in meta_model.items():
    if meta_model_key == "_id":
      model_uid = ObjectId(meta_model_value)
    elif meta_model_key == "dashboardpages":
      dashboard_style = check_dashboard_visualization_style(meta_model_value)
      if viz_tool == 'grafana':
        dashboards = create_dashboards_for_grafana(meta_model_value, dashboard_style, model_uid)
      else:
        dashboards = create_dashboards_for_kibana(meta_model_value, dashboard_style, model_uid)
  logger.debug("Meta Model Interpreted ")
  logger.debug("Style Recognized!")
  logger.debug(dashboard_style)
  logger.debug("Panels Created")
  logger.debug("Final Dashboards Ready")
  return dashboards






