import os


class Grid:
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
