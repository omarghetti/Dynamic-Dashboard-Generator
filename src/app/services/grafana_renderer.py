import os
from src.app.utils.utils import load_template
from src.app.services.http_dispatcher import post_grafana_dashboard

current_path = os.path.dirname(__file__)
grafana_dash_path = os.path.join(current_path, 'templates/grafana_dashboard')
grafana_panels_path = os.path.join(current_path, 'templates/grafana_panels')


def load_grafana_templates(dashboards, dashboard_style):
  rendered_dashboards = []
  dashboard_url = ""
  for item in dashboards:
    dash_template = load_template(grafana_dash_path, 'grafana_dashboard.json')
    if dash_template is not None:
      rendered_dashboard = render_grafana_templates(dash_template, item, dashboard_url)
      rendered_dashboards.append(rendered_dashboard)
    else:
      raise ValueError("grafana-renderer - render_grafana_templates: error loading dashboard template")
    response = post_grafana_dashboard(rendered_dashboard)
    dashboard_url = response.url
  return rendered_dashboards


def render_grafana_templates(dash_to_render, concrete_dash, dashboard_url):
  rendered_dashboard = dash_to_render.render(panels=concrete_dash.panels, dashboard=concrete_dash, url=dashboard_url)
  return rendered_dashboard




