import pytest
from src.app.utils.db import mongodb_connect
from simple_settings import settings
from src.app.services.MetaModelInterpreter import meta_model_interpreter
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.panel import Panel
from src.app.models.grid_model import Grid
from src.app.utils.logger import get_logger


def test_decoded_message():
  mongodb_connect(settings.MONGO_URI, connection_alias=settings.APP_NAME)
  message = "{\"_id\":\"60118b66ad58f40f597dd6a0\",\"dashboardpages\":[\"60118b66ad58f40f597dd69f\"]}"
  dashboards = meta_model_interpreter(message)
  assert dashboards[0].dashboard_style == "RepeatedStyle"
  assert len(dashboards) == 1
  assert len(dashboards[0].panels) == 12


