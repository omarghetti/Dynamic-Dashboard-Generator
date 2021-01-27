from src.app.models.base_models import *


##Basic CRUD Operations for MongoDB Models


def count_dash():
    counter = DashboardGlobal.objects.all().count()
    return counter


def find_all_dash():
    return DashboardGlobal.objects.all()


def find_dash(name):
    return DashboardGlobal.objects.get({'_id': name})


def delete_dash(name):
    return DashboardGlobal.objects.get({'_id': name}).delete()


def save_dash(DashboardGlobal):
    return DashboardGlobal.save()


def find_item(name):
  return DashboardItem.objects.get({'_id': name})


def find_page(name):
  return DashboardPage.objects.get({'_id': name})


def find_viz(name):
  return Visualization.objects.get({'_id': name})


def find_KPI(name):
  return KPI.objects.get({'_id': name})
