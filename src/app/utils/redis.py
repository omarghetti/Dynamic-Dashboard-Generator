# -*- coding: utf-8 -*-
import redis
from simple_settings import settings

def redis_connect(host, port, db, *args):
    return redis.Redis(host=host, port=port, db=db, *args)

connection = redis_connect(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)