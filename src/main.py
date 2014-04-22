import logging
import os

import webapp2
import jinja2

from forecast import is_raining
from photo import location_photo
from location import Location

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])

class MainHandler(webapp2.RequestHandler):

  def get(self):
    template = JINJA_ENVIRONMENT.get_template('main.html')
    location = Location(self.request.headers)
    variables = {
            'photo': location_photo(location.name),
            'location': location.name,
            'is_raining': is_raining(location),
            }

    self.response.write(template.render(variables))

app = webapp2.WSGIApplication(
    [
     ('/', MainHandler),
    ],
    debug=True)
