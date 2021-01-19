import requests
import json
from simple_settings import settings
from src.app.utils.logger import get_logger

grafana_auth = (settings.GRAFANA_USER, settings.GRAFANA_PASSWORD)

grafanaHeaders = {"Accept": "application/json",
                  "Content-Type": "application/json"}

def post_grafana_dashboard(final_dashboard):
  postUrl = settings.GRAFANA_DASHBOARD_URL+"api\dashboard\db"
  response = requests.post(url=postUrl, data=final_dashboard, headers=grafanaHeaders,
                           auth=grafana_auth)
  return response



