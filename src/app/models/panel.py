import os
import uuid
import random


class Panel:
  def __init__(self, title, kpi_related, grid_position, panel_type):
    self.title = title
    self.kpi_related = kpi_related
    self.grid_position = grid_position
    self.panel_type = panel_type

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


class KibanaPanel(Panel):
  def __init__(self, title, kpi_related, grid_position, panel_type, queryList):
    super().__init__(title, kpi_related, grid_position, panel_type)
    self.id = uuid.uuid4()
    self.queryList = queryList


class GrafanaPanel(Panel):
  def __init__(self, title, kpi_related, grid_position, panel_type, queryList):
    super().__init__(title, kpi_related, grid_position, panel_type)
    self.id = random.randint(0, 100000)
    self.queryList = queryList
