import os
import uuid


class Panel:
  def __init__(self, title, kpi_related, grid_position, panel_type):
    self.id = uuid.uuid1()
    self.title = title
    self.kpi_related = kpi_related
    self.grid_position = grid_position
    self.panel_type = panel_type

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
