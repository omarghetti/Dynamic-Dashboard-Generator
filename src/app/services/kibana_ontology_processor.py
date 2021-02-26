from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel
from owlready2 import *
import json

def query_ontology_for_kibana(dashboards):
  onto = get_ontology("file://src/app/services/Ontology/KPIOnto.owl").load()

