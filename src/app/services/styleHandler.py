from src.app.models.base_models import *
from src.app.repositories.CRUD import *
from src.app.utils.logger import get_logger
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel
from bson import ObjectId

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
      dashboardpage = find_page(ObjectId(page))
      items_list = dashboardpage.items
      if len(
        items_list) > 1:  ## if we have only one dashboard_item, we stick to pyramidal style to fill the whole first line of the dashboard
        n_root_viz = len(items_list) / 2
        for item in dashboardpage.items:
          if item['width'] == 100 / n_root_viz:
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
    meta_page = find_page(ObjectId(page))
    for item in meta_page.items:
      meta_item = find_item(item['item'])
      panels, last_height = create_panels(meta_item.visualizations, item['width'], last_height)
      panel_list.append(panels)
    concrete_dashboard = Meta_Dashboard(model_uid, dashboardstyle, panel_list)
    dashboardlist.append(concrete_dashboard)
    last_height = 0
  return dashboardlist


##Panel Creation, class Panel and Grid populated to create the support structure for the ontology
def create_panels(items_list, width, last_height):
  support_list = []
  if isinstance(items_list, dict):
    support_list.append(items_list)
  else:
    support_list = items_list.copy()
  panels = []
  x = 0
  w = 0
  h = 0
  y = last_height
  for item in support_list:
    viz_to_process = find_viz(item['viz'])
    h = (8 / item['high_in_item']) * 100  # we keep 8 as standard for height value to maintain readability of the panels
    w = (((24 / item['width_in_item']) * 100) / width) * 100  # grafana limit for width in dashboard is 24 columns
    if w != 24:
      x += w
      y = 0
    else:
      x = 0
      y += h
    grid = Grid(x, y, w, h)
    if isinstance(viz_to_process, SimpleVisualization):
      new_panel = Panel(viz_to_process.name, viz_to_process.kpis, grid)
    else:
      summary_viz = find_viz(viz_to_process.summary_visualization)
      new_panel = Panel(summary_viz.name, summary_viz.kpis, grid)
    last_height = y
    panels.append(new_panel)
  return panels, last_height
