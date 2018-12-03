# -*- coding: utf-8 -*-

from bson import ObjectId
from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, ObjectId):
      return str(obj)
    return super(CustomJSONEncoder, self).default(obj)
