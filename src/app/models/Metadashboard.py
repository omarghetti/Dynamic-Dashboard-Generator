import os


class Meta_Dashboard:
  def __init__(self, dashboard_id, dashboard_style, panels):
    self.dashboard_id = dashboard_id
    self.dashboard_style = dashboard_style
    self.panels = panels

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
