import src.app.models.base_models as bm
from src.app.repositories.CRUD import *
from src.app.utils.logger import get_logger
from src.app.models.Metadashboard import Meta_Dashboard
from src.app.models.grid_model import Grid
from src.app.models.panel import Panel
from src.app.services.grafana_ontology_processor import query_ontology_for_grafana
from src.app.services.kibana_ontology_processor import query_ontology_for_kibana
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
def create_dashboards_for_grafana(pages_list, dashboardstyle, model_uid):
  dashboardlist = []
  last_grid_position = Grid(0, 0, 0, 0)
  for page in pages_list:
    panel_list = []
    meta_page = find_page(ObjectId(page))
    for item in meta_page.items:
      meta_item = find_item(item['item'])
      panels, last_grid_position = create_panels_for_grafana(meta_item.visualizations, item['width'], last_grid_position, dashboardstyle)
      panel_list.append(panels)
    concrete_dashboard = Meta_Dashboard(model_uid, dashboardstyle, panel_list)
    dashboardlist.append(concrete_dashboard)
  return dashboardlist


def create_dashboards_for_kibana(pages_list, dashboard_style, model_uid):
  dashboardlist = []
  last_grid_position = Grid(0, 0, 0, 0)
  for page in pages_list:
    panel_list = []
    meta_page = find_page(ObjectId(page))
    for item in meta_page.items:
      meta_item = find_item(item['item'])
      panels, last_grid_position = create_panels_for_kibana(meta_item.visualizations, item['width'], last_grid_position, dashboard_style)
      panel_list.append(panels)
    concrete_dashboard = Meta_Dashboard(model_uid, dashboard_style, panel_list)
    dashboardlist.append(concrete_dashboard)
  return dashboardlist


##Panel Creation, class Panel and Grid populated to create the support structure for OP and Templating
def create_panels_for_grafana(items_list, width, last_grid_position, dashboardstyle):
  support_list = []
  position = 0
  if isinstance(items_list, dict):
    support_list.append(items_list)
  else:
    support_list = items_list.copy()
  panels = []
  if last_grid_position.x == 24:
    x = 0
    y = last_grid_position.y + 8
  else:
    x = last_grid_position.x
    y = last_grid_position.y
  for item in support_list:
    viz_to_process = find_viz(item['viz'])
    h = round((8 / 100.0) * item[
      'high_in_item'])
    w = round(
      (((24 / 100.0) * item['width_in_item']) / 100.0) * width)
    # grafana limit for width in dashboard is 24 columns
    grid = Grid(x, y, w, h)
    if dashboardstyle == 'PyramidalStyle':
      if h == 8:
        x += w
      else:
        y += h
        if y % 8 == 0:
          if position == len(support_list) - 1:
            y -= 8
            x += w
          else:
            y -= h
            x += w
    else:
      if h == 8:
        x += w
      else:
        y += h
        if y % 8 == 0:
          y -= 8
          x += w
    position += 1
    next_panel_reference = Grid(x, y, w, h)
    if isinstance(viz_to_process, bm.SimpleVisualization):
      panel_name = query_ontology_for_grafana(viz_to_process)
      new_panel = Panel(viz_to_process.name, viz_to_process.kpis, grid, panel_name)
    elif isinstance(viz_to_process, bm.ComposedVisualization):
      panel_name = query_ontology_for_grafana(viz_to_process.summary_visualization)
      new_panel = Panel(viz_to_process.summary_visualization.name, viz_to_process.summary_visualization.kpis, grid
                        , panel_name)
    panels.append(new_panel)
  return panels, next_panel_reference


def create_panels_for_kibana(items_list, width, last_grid_position, dashboard_style):
  support_list = []
  position = 0
  if isinstance(items_list, dict):
    support_list.append(items_list)
  else:
    support_list = items_list.copy()
  panels = []
  if last_grid_position.x == 24:
    x = 0
    y = last_grid_position.y + 8
  else:
    x = last_grid_position.x
    y = last_grid_position.y
  for item in support_list:
    viz_to_process = find_viz(item['viz'])
    h = round((15 / 100.0) * item[
      'high_in_item']) # we keep 8 as standard for height value to maintain readability of the panels
    w = round((((48 / 100.0) * item['width_in_item']) / 100.0) * width ) # kibana limit for width in dashboard is 24 columns
    grid = Grid(x, y, w, h)
    if dashboard_style == 'PyramidalStyle':
      if h == 15:
        x += w
      else:
        y += h
        if y % 15 == 0:
          if position == len(support_list) - 1:
            y -= 15
            x += w
          else:
            y -= h
            x += w
    else:
      if h == 15:
        x += w
      else:
        y += h
        if y % 15 == 0:
          y -= 15
          x += w
    next_panel_reference = Grid(x, y, w, h)
    if isinstance(viz_to_process, bm.SimpleVisualization):
      panel_name = query_ontology_for_kibana(viz_to_process)
      new_panel = Panel(viz_to_process.name, viz_to_process.kpis, grid, panel_name)
    elif isinstance(viz_to_process, bm.ComposedVisualization):
      panel_name = query_ontology_for_kibana(viz_to_process.summary_visualization)
      new_panel = Panel(viz_to_process.summary_visualization.name, viz_to_process.summary_visualization.kpis,
                        grid, panel_name)
    panels.append(new_panel)
  return panels, next_panel_reference
