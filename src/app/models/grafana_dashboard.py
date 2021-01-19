import os


class grafana_dashboard:
  def __init__(self, title, uid, id):
    self.title = title
    self.uid = uid
    self.id = id

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


