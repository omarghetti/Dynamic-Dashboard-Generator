from src.app.repositories.CRUD import *
from owlready2 import *
from src.app.models.base_models import SimpleKPI, DerivedKPI


def query_ontology_for_grafana(viz):
  onto = get_ontology("file://src/app/services/ontology/KPIOnto.owl").load()
  if isinstance(viz.kpis[0], SimpleKPI) or isinstance(viz.kpis[0], DerivedKPI):
    kpi_to_process = viz.kpis[0]
  else:
    kpi_to_process = find_KPI(viz.kpis[0])
  query_result = onto.search_one(acronym=kpi_to_process.name)
  if query_result.unitOfMeasure[0] == '#':
    return "Graph"
  elif query_result.unitOfMeasure[0] == 'Percent':
    return "Gauge"
  elif query_result.unitOfMeasure[0] == 'Mhz':
    return "Graph"
  else:
    return "Graph"






