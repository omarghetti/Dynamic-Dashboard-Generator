import requests
from simple_settings import settings

grafana_auth = (settings.GRAFANA_USER, settings.GRAFANA_PASSWORD)

grafanaHeaders = {"Accept": "application/json",
                  "Content-Type": "application/json"}

kibanaHeaders = {"kbn-xsrf": ""}


def post_grafana_dashboard(final_dashboard):
  postUrl = settings.GRAFANA_DASHBOARD_URL + "api/dashboards/db"
  response = requests.post(url=postUrl, data=final_dashboard, headers=grafanaHeaders,
                           auth=grafana_auth)
  return response


def post_kibana_dashboard(final_dashboard):
  postUrl = settings.KIBANA_DASHBOARD_URL + "api/saved_objects/dashboard"
  response = requests.post(url=postUrl, data=final_dashboard, headers=kibanaHeaders)
  return response


def post_kibana_visualizations(visualization, vizId):
  postUrl = settings.KIBANA_DASHBOARD_URL + "api/saved_objects/visualization/"+str(vizId)
  response = requests.post(url=postUrl, data=visualization, headers=kibanaHeaders)
  return response
