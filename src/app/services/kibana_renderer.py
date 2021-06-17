import os
from src.app.utils.utils import load_template
from src.app.services.http_dispatcher import post_kibana_visualizations, post_kibana_dashboard
from src.app.utils.logger import get_logger

logger = get_logger(__name__)

current_path = os.path.dirname(__file__)
kibana_dash_path = os.path.join(current_path, 'templates/kibana_dashboard')
kibana_panels_path = os.path.join(current_path, 'templates/kibana_dashboard/kibana_panels')


def load_kibana_templates(dashboards, dashboard_style, datasource):
  rendered_dashboards = []
  for item in dashboards:
    dash_template = load_template(kibana_dash_path, 'kibana_dashboard.json')
    if dash_template is not None:
      rendered_dashboard = render_kibana_templates(dash_template, item)
      rendered_dashboards.append(rendered_dashboard)
    else:
      raise ValueError("kibana-renderer - render_kibana_templates: error loading dashboard template")
    response = post_kibana_dashboard(rendered_dashboard, item.dashboard_id)
    dashboard_url = response.url
  return rendered_dashboards


def render_kibana_templates(dash_template, item):
  render_kibana_viz(item.panels, item)
  rendered_dashboard = dash_template.render(panels=item.panels, dashboard=item)
  return rendered_dashboard


def render_kibana_viz(panels, dashboard):
  for item in panels:
    for panel in item:
      template_name = 'kibana_'+panel.panel_type+'.json'
      panel_template = load_template(kibana_panels_path, template_name)
      if panel_template is not None:
        rendered_panel = panel_template.render(panel=panel, links=dashboard.links)
        response = post_kibana_visualizations(rendered_panel, panel.id)
        logger.debug(response)
      else:
        raise ValueError("kibana-renderer - render_kibana_viz: error loading panel template")



