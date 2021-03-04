from jinja2 import Environment, FileSystemLoader


def load_template(template_directory, template_name):
    file_loader = FileSystemLoader(template_directory)
    env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_name)
    return template
