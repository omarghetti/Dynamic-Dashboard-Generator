from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel
from owlready2 import *
from src.app.repositories.CRUD import *
import json

def query_ontology_for_kibana(viz):
  onto = get_ontology("file://src/app/services/ontology/KPIOnto.owl").load()
  kpi_to_process = find_KPI(viz.kpis[0])
  query_result = onto.search_one(acronym=kpi_to_process.name)
  if query_result.unitOfMeasure == "#":
    return "Graph"
  elif query_result.unitOfMeasure == "Percent":
    return "Gauge"
  elif query_result.unitOfMeasure == "Mhz":
    return "Graph"
  else:
    return "Graph"

