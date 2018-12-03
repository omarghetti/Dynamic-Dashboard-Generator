import os
from bson import ObjectId
from flask import Flask
from flask_cors import CORS
from app.utils.json import CustomJSONEncoder
from app.utils.db import mongodb_connect
from app.routes import api

def create_app(test_config=None):
  app = Flask(__name__)
  CORS(app)
  mongo_uri = os.environ.get('MONGO_URI')

  app.config.from_mapping(
    SECRET_KEY='dev',
    MONGO_URI=mongo_uri,
  )

  mongodb_connect(app.config['MONGO_URI'], __name__)

  app.register_blueprint(api.api)
  app.json_encoder = CustomJSONEncoder

  return app
