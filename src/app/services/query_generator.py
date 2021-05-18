import json

from src.app.models.base_models import SimpleKPI, DerivedKPI
from src.app.models.prometheus_models import PromExpression
from src.app.repositories.CRUD import find_KPI


def query_generator(viz, datasource):
  if (datasource == 'elasticsearch'):
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
  return 0
