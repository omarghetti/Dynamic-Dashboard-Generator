# -*- coding: utf-8 -*-

from environs import Env

env = Env()
env.read_env()

APP_NAME = env.str('APP_NAME')
DEBUG = env.bool('DEBUG', False)

KAFKA_BROKERS = env.list('KAFKA_BROKERS')
KAFKA_GROUP = env.str('KAFKA_GROUP')
KAFKA_TOPIC = env.str('KAFKA_TOPIC')

GRAFANA_USER = env.str('GRAFANA_USER')
GRAFANA_PASSWORD = env.str('GRAFANA_PASSWORD')
GRAFANA_DASHBOARD_URL = env.str('GRAFANA_DASHBOARD_URL')
KIBANA_DASHBOARD_URL = env.str('KIBANA_DASHBOARD_URL')
MONGO_URI = env.str('MONGO_URI')
CONNECTION_ALIAS = env.str('CONNECTION_ALIAS')

REDIS_HOST = env.str('REDIS_HOST')
REDIS_PORT = env.str('REDIS_PORT')
REDIS_DB = env.str('REDIS_DB')

QUEUES = env.list('QUEUES')
