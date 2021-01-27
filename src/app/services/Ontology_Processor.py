from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel
import rdflib
import json

def query_ontology(dashboards):
  g = rdflib.Graph()

