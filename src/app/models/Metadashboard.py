import os


class Meta_Dashboard:
  def __init__(self, dashboard_id, dashboard_style, panels):
    self.dashboard_id = dashboard_id
    self.dashboard_style = dashboard_style
    self.panels = panels

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


class Grafana_Dashboard(Meta_Dashboard):
  def __init__(self, dashboard_id, dashboard_style, panels, links):
    super().__init__(dashboard_id, dashboard_style, panels)
    self.link = links


class Kibana_Dashboard(Meta_Dashboard):
  def __init__(self, dashboard_id, dashboard_style, panels, links):
    super().__init__(dashboard_id, dashboard_style, panels)
    self.links = links
