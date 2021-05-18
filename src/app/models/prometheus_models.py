import os


class PromExpression():

  def __init__(self, expression_tag, expression_query):
    self.expression_tag = expression_tag
    self.expression_query = expression_query

    class Meta:
      connection_alias = os.environ.get('APP_NAME')
