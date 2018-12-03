# -*- coding: utf-8 -*-
from pymodm import connect

def mongodb_connect(mongo_uri, connection_alias):
  connect(mongo_uri, alias=connection_alias)
