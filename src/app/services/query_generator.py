import json

from src.app.models.base_models import SimpleKPI, DerivedKPI
from src.app.models.elasticsearch_models import ESAggregations, DateHistogram, ESMetric, ESquery
from src.app.models.prometheus_models import PromExpression
from src.app.repositories.CRUD import find_KPI


def query_generator(viz, datasource):
  if (datasource == 'Elasticsearch'):
    queryList = query_generator_elasticsearch(viz)
  if (datasource == 'Prometheus'):
    queryList = query_generator_prometheus(viz)
  return queryList


def query_generator_prometheus(viz):
  queryList = []
  with open("src/app/services/query_dictionary/prometheus_queryref.json") as query_dict:
    data = json.load(query_dict)
    for kpi in viz.kpis:
      if isinstance(kpi, SimpleKPI) or isinstance(kpi, DerivedKPI):
        kpi_to_process = kpi
      else:
        kpi_to_process = find_KPI(kpi)
      Prom_query_tag = kpi_to_process.name
      Prom_query_expression = data[Prom_query_tag]
      Prom_expression = PromExpression(Prom_query_tag, Prom_query_expression)
      queryList.append(Prom_expression)
  return queryList


def query_generator_elasticsearch(viz):
  queryList = []
  with open("src/app/services/query_dictionary/ES_queryref.json") as query_dict:
    data = json.load(query_dict)
    for kpi in viz.kpis:
      aggs = []
      metrics = []
      new_dh = None
      if isinstance(kpi, SimpleKPI) or isinstance(kpi, DerivedKPI):
        kpi_to_process = kpi
      else:
        kpi_to_process = find_KPI(kpi)
      kpi_name = kpi_to_process.name
      query_data = json.loads(data[kpi_name])
      for item in query_data['aggregations']:
        new_agg = ESAggregations(field=item['field'])
        aggs.append(new_agg)
        new_dh = DateHistogram(interval=item['date_histogram']['interval'])
        new_metric = ESMetric(field=query_data['metric']['field'], operator=query_data['metric']['operator'])
        metrics.append(new_metric)
      new_query = ESquery(select=query_data['select'], aggregations=aggs, date_histogram=new_dh, metrics=metrics)
      queryList.append(new_query)
  return queryList



