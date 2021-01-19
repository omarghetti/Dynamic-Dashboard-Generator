import os


class DashboardStyle:
  def __init__(self, dashboard_id, dashboard_style):
    self.dashboard_id = dashboard_id
    self.dashboard_style = dashboard_style

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
