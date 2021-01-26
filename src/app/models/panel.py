import os


class Panel:
  def __init__(self, title, kpi_related, grid_position):
    self.title = title
    self.kpi_related = kpi_related
    self.grid_position = grid_position

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
