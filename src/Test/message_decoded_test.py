import pytest
from src.app.utils.db import mongodb_connect
from simple_settings import settings
from src.app.services.MetaModelInterpreter import Meta_Model_Interpreter
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.panel import Panel
from src.app.models.grid_model import Grid

def test_decoded_message():
  mongodb_connect(settings.MONGO_URI, connection_alias=settings.APP_NAME)
  message = "{\"_id\":\"6001a550ec3a465aaed372c8\",\"dashboardpages\":[\"6001a550ec3a465aaed372c7\"]}"
  dashboards = Meta_Model_Interpreter(message)
  assert dashboards[0].dashboard_style == "RepeatedStyle"
  assert len(dashboards) == 1
  assert len(dashboards[0].panels) > 10

