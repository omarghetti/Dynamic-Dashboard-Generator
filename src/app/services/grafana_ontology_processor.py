from src.app.repositories.CRUD import *
from owlready2 import *


def query_ontology_for_grafana(viz):
  onto = get_ontology("file://src/app/services/Ontology/KPIOnto.owl").load()

