from bson import ObjectId
from src.app.services.styleHandler import check_dashboard_visualization_style, \
  create_dashboards_for_grafana, create_dashboards_for_kibana
from src.app.services.http_dispatcher import post_grafana_dashboard, post_kibana_dashboard
from src.app.services.grafana_renderer import *
from src.app.services.kibana_renderer import *
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
  if viz_tool == 'grafana':
    final_dashboards = load_grafana_templates(dashboards, dashboard_style)
    for i in final_dashboards:
      post_grafana_dashboard(i)
  else:
    final_dashboards = load_kibana_templates(dashboards, dashboard_style)
    for i in final_dashboards:
      post_kibana_dashboard(i)
  return dashboards






