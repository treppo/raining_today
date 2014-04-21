import logging
import os

import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])

class MainHandler(webapp2.RequestHandler):

  def get(self):
    template = JINJA_ENVIRONMENT.get_template('main.html')
    variables = {
            'location': 'Dublin',
            'is_raining': 'YUP!',
            }

    self.response.write(template.render(variables))

app = webapp2.WSGIApplication(
    [
     ('/', MainHandler),
    ],
    debug=True)
