from src.app.models.base_models import *
from src.app.repositories.CRUD import *
from src.app.utils.logger import get_logger
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel

logger = get_logger(__name__)


##Verifiyng the style related to the Meta_Model. We know from styles implementation
# that if we have more than one page we are looking to a Nested Style Dashboard
# while if we are facing a Repeated Style Dashboard, root items will be represented in the first row
# with size proportional to the number of root items. in the remaining cases, it's a Pyramidal Style
def check_dashboard_visualization_style(pages_list):
  if len(pages_list) > 1:  ##only nested dashboards have more than one page per global
    return "NestedStyle"
  else:
    for page in pages_list:
      dashboardpage = find_page(page)
      if len(dashboardpage["item"]) > 2:  ## if we have only one dashboard_item, we stick to pyramidal style to fill the whole first line of the dashboard
        n_main_viz = len(dashboardpage["item"])/2
        for item in dashboardpage["item"]:
          if item["width"] == 100/n_main_viz:
            return "RepeatedStyle"
          else:
            return "PyramidalStyle"
      else:
        return "PyramidalStyle"


##cycling the meta-model to create the agnostic model to support final dashboard creation.
# this agnostic model will be processed inside the ontology to create the
# right panels for the final dashboard
def create_dashboards(pages_list, dashboardstyle, model_uid):
  dashboardlist = []
  last_height = 0
  for page in pages_list:
    panel_list = []
    meta_page = find_page(page)
    for item in meta_page["item"]:
      meta_item = find_item(item)
      panels, last_height = create_panels(meta_item["visualizations"], meta_item["width"], last_height)
      panel_list.append(panels)
    concrete_dashboard = Meta_Dashboard(model_uid, dashboardstyle, panel_list)
    dashboardlist.append(concrete_dashboard)
    last_height = 0
  return dashboardlist

##Panel Creation, class Panel and Grid populated to create the support structure for the ontology
def create_panels(items_list, width, lastheight):
  panels = []
  x, w, h = 0
  y = lastheight
  for item in items_list:
    viz_to_process = find_viz(item["viz"])
    h = (8/item["high_in_item"])*100                       #we keep 8 as standart for height value to maintain readability of the panels
    w = (((24/item["width_in_item"])*100)/width)*100       #grafana limit for width in dashboard is 24 columns
    if w != 24:
      x += w
      y = 0
    else:
      x = 0
      y += h
    grid = Grid(x, y, w, h)
    new_panel = Panel(item["_id"], viz_to_process["kpis"][0], grid)
    lastheight = y
    panels.append(new_panel)
  return panels, lastheight











