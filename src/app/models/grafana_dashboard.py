import os


class grafana_dashboard:
  def __init__(self, title, uid, db_id):
    self.title = title
    self.uid = uid
    self.db_id = db_id

    class Meta:
      connection_alias = os.environ.get('APP_NAME')


