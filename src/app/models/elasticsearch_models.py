import os


class ESAggregations():
  def __init__(self, field, value):
    self.field = field
    self.value = value

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


class ESMetric():
  def __init__(self, value, operator, field):
    self.value = value
    self.field = field
    self.operator = operator

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


class DateHistogram():
  def __init__(self, interval):
    self.interval = interval

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


class ESquery():
  def __init__(self, metrics, date_histogram, aggregations, select):
    self.metrics = metrics
    self.date_histogram = date_histogram
    self.aggregations = aggregations
    self.select = select

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
