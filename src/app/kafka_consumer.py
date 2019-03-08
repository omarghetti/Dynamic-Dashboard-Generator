#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
from confluent_kafka import Consumer, KafkaError, KafkaException
from simple_settings import settings
from utils.db import mongodb_connect
import services.dashboard as dashboard_service
from utils.logger import get_logger

def handle_sigterm(*args):
  raise KeyboardInterrupt()

def main(*args):
  signal.signal(signal.SIGTERM, handle_sigterm)
  logger = get_logger(__name__)
  mongodb_connect(settings.MONGO_URI, connection_alias=settings.APP_NAME)

  conf = {
    'bootstrap.servers': ','.join(settings.KAFKA_BROKERS),
    'group.id': settings.KAFKA_GROUP,
    'session.timeout.ms': 6000,
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True,
  }

  consumer = Consumer(**conf, logger=logger)
  consumer.subscribe([settings.KAFKA_TOPIC])

  try:
    while True:
      message = consumer.poll(timeout=0.5)
      if message is None:
        continue
      elif not message.error():
        dashboard_service.handle_monitoring_request(message)
      elif message.error().code() == KafkaError._PARTITION_EOF:
        logger.debug('End of partition reached %s/%s', message.topic(), message.partition())
      else:
        raise KafkaException(message.error())

  except KeyboardInterrupt:
    logger.info('Shutting down Kafka consumer...')
  finally:
    consumer.close()

if __name__ == '__main__':
  main()
