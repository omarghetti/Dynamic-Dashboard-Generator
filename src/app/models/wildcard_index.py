import os
import datetime
import uuid


class Wildcard_Index:
  def __init__(self, name):
    self.id = uuid.uuid4()
    self.name = name

  class Meta:
    connection_alias = os.environ.get("APP_NAME")
