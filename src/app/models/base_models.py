import os
from pymodm import MongoModel, ReferenceField, fields


class KPI(MongoModel):
  name = fields.CharField(required=True)

  class Meta:
    connection_alias = "dynamic_dashboard_generator"


class SimpleKPI(KPI):
  kpi_id = fields.DictField(required=True)
  target = fields.DictField(required=True)


class DerivedKPI(KPI):
  source_kpis = fields.ListField(field=ReferenceField(KPI), required=True)
  transformation_function = fields.CharField(required=True)
  tf_arguments = fields.DictField(required=False)


class Visualization(MongoModel):
  name = fields.CharField(required=True)

  class Meta:
    connection_alias = "dynamic_dashboard_generator"


class SimpleVisualization(Visualization):
  kpis = fields.ListField(field=ReferenceField(KPI), required=True)


class ComposedVisualization(Visualization):
  summary_visualization = fields.ReferenceField(SimpleVisualization, required=False)
  composing_visualizations = fields.ListField(field=ReferenceField(Visualization), required=True)


class DashboardItem(MongoModel):
  visualizations = fields.ListField(required=True)
  item_number = fields.FloatField()
  scrolling = fields.FloatField(required=False)

  class Meta:
    connection_alias = "dynamic_dashboard_generator"


class DashboardPage(MongoModel):
  items = fields.ListField()
  link_son = fields.ListField()
  link_father = fields.ListField()

  class Meta:
    connection_alias = "dynamic_dashboard_generator"


class DashboardGlobal(MongoModel):
  dashboardpages = fields.ListField(required=True)

  class Meta:
    connection_alias = "dynamic_dashboard_generator"
