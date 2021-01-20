from src.app.models.base_models import *
from src.app.repositories.CRUD import *
from src.app.utils.logger import get_logger

logger = get_logger(__name__)


##Verifiyng the style related to the Meta_Model
def check_dashboard_visualization_style(pages_list):
  if len(pages_list) > 1:  ##only nested dashboards have more than one page per global
    return "NestedStyle"
  else:
    for page in pages_list:
      dashboardpage = find_page(page)
      if len(dashboardpage["item"]) > 1:  ## if we have only one dashboard_item, we stick to pyramidal style to fill the whole first line of the dashboard
        n_main_viz = len(dashboardpage["item"])/2
        for item in dashboardpage["item"]:
          if item["width"] == 100/n_main_viz:
            return "RepeatedStyle"
          else:
            return "PyramidalStyle"
      else:
        return "PyramidalStyle"
