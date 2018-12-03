# -*- coding: utf-8 -*-

from flask import current_app, Blueprint, request, abort, jsonify, make_response
from cerberus import Validator

api = Blueprint('api', __name__, url_prefix='/api/v1')
schema = {
  'service': {
    'type': 'dict',
    'schema': {
      'name': { 'type': 'string', 'required': True, },
      'instances': { 'type': 'list', 'required': True, },
    },
    'required': True,
  },
  'goals': {
    'type': 'list',
    'schema': { 'type': 'string' },
    'required': True,
  },
  'cloud_properties': {
    'type': 'list',
    'schema': { 'type': 'string' },
    'required': True,
  },
  'monitoring_request_id': { 'type': 'string', 'required': True, },
}
validator = Validator(schema)

@api.route('/generate-dashboard', methods=['POST'], strict_slashes=False)
def generate_dashboard():
  """Generate a dashboard based on monitoring request details."""
  monitoring_details = request.json
  is_valid = validator.validate(monitoring_details)
  if is_valid:
    return make_response(jsonify(message='Dashboard generated.'), 201)
  else:
    return make_response(jsonify(message='The validation of the payload failed.', errors=validator.errors), 400)
