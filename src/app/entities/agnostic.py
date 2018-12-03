# -*- coding: utf-8 -*-
from datetime import datetime
from pymodm import MongoModel, EmbeddedMongoModel, fields
import os

class Metric(EmbeddedMongoModel):
  """The class which represents a metric."""
  cloud_property = fields.CharField(required=True)

  class Meta:
    connection_alias = os.environ.get('FLASK_APP')

  def __repr__(self):
    return '{}(cloud_property={!r})'.format(self.__class__.__name__, self.cloud_property)

class Visualization(MongoModel):
  """The class which represents a visualization."""
  title = fields.CharField(required=True)
  type = fields.CharField(choices=('gauge', 'chart'), required=True)
  metric = fields.EmbeddedDocumentField(Metric, required=True)
  created_at = fields.DateTimeField(required=True)
  updated_at = fields.DateTimeField(required=False)

  class Meta:
    connection_alias = os.environ.get('FLASK_APP')

  def __repr__(self):
    return '{}(title={!r}, type={!r}, created_at={!r}, updated_at={!r})'.format(self.__class__.__name__, self.title, self.type, self.created_at, self.updated_at)

class Dashboard(MongoModel):
  """The class which represents a dashboard."""
  title = fields.CharField(required=True)
  visualizations = fields.ListField(ReferenceField(Visualization), blank=False, required=True)
  monitoring_request_id = fields.ObjectIdField(required=True)
  created_at = fields.DateTimeField(required=True)
  updated_at = fields.DateTimeField(required=False)

  class Meta:
    connection_alias = os.environ.get('FLASK_APP')

  def __repr__(self):
    return '{}(title={!r}, visualizations={!r}, created_at={!r}, updated_at={!r})'.format(self.__class__.__name__, self.title, self.visualizations, self.created_at, self.updated_at)
