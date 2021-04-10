import os
from src.app.utils.utils import load_template

current_path = os.path.dirname(__file__)
kibana_dash_path = os.path.join(current_path, 'templates/kibana_dashboard')
kibana_panels_path = os.path.join(current_path, 'templates/kibana_panels')


def load_kibana_templates(dashboards, dashboard_style):
  rendered_dashboards = []
  for item in reversed(dashboards):
    dash_template = load_template(kibana_dash_path, 'kibana_dashboard.json')
    if dash_template is not None:
      rendered_dashboard = render_kibana_templates(dash_template, item)
      rendered_dashboards.append(rendered_dashboard)
    else:
      raise ValueError("kibana-renderer - render_kibana_templates: error loading dashboard template")
  return rendered_dashboards


def render_kibana_templates(dash_template, item):
  render_kibana_viz(item.panels)
  rendered_dashboard = dash_template.render(panels=item.panels, dashboard=item)
  return rendered_dashboard


def render_kibana_viz(panels):
  for item in panels:
    template_name = 'kibana_'+item.panel_type+'.json'
    panel_template = load_template(kibana_panels_path, template_name)
    if panel_template is not None:
      rendered_panel = panel_template.render(panel=item)
    else:
      raise ValueError("kibana-renderer - render_kibana_viz: error loading panel template")



