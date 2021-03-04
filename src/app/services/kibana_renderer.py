import os
from src.app.utils.utils import load_template

current_path = os.path.dirname(__file__)
grafana_dash_path = os.path.join(current_path, 'templates/kibana_dashboard')
grafana_panels_path = os.path.join(current_path, 'templates/kibana_panels')


def load_kibana_templates(dashboards, dashboard_style):
  for item in dashboards:
    dash_template = load_template()
