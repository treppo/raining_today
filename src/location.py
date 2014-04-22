class Location:

    DEFAULT_NAME = 'dublin'
    DEFAULT_COORDINATES = '53.3494299,-6.2600969'

    def __init__(self, request_headers):
        self.name = self.__name(request_headers)
        self.lat, self.lon = self.__coordinates(request_headers)

    def __name(self, request_headers):
        from_headers = request_headers.get('X-AppEngine-City')
        return (from_headers or self.DEFAULT_NAME).capitalize()

    def __coordinates(self, request_headers):
        from_headers = request_headers.get('X-AppEngine-CityLatLong')
        return (from_headers or self.DEFAULT_COORDINATES).split(',')
