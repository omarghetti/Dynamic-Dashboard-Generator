import uuid

from jinja2 import Environment, FileSystemLoader


def calculate_uuid():
  rnd_uuid = uuid.uuid4()
  return rnd_uuid


def load_template(template_directory, template_name):
  file_loader = FileSystemLoader(template_directory)
  env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
  env.globals['uuid'] = calculate_uuid
  template = env.get_template(template_name)
  return template
