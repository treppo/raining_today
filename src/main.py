import logging
import os

import webapp2
import jinja2

from forecast import is_raining
from photo import location_photo

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
    extensions=['jinja2.ext.autoescape'])

DEFAULT_CITY = 'dublin'
DEFAULT_COORDINATES = '53.3494299,-6.2600969'

class MainHandler(webapp2.RequestHandler):

  def get(self):
    template = JINJA_ENVIRONMENT.get_template('main.html')
    city = self.request.headers.get('X-AppEngine-City') or DEFAULT_CITY
    coordinates = self.request.headers.get('X-AppEngine-CityLatLong') or DEFAULT_COORDINATES
    variables = {
            'photo': location_photo(coordinates, city),
            'location': city.capitalize(),
            'is_raining': is_raining(coordinates),
            }

    self.response.write(template.render(variables))

app = webapp2.WSGIApplication(
    [
     ('/', MainHandler),
    ],
    debug=True)
