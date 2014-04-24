import os

import flickrapi

API_KEY = os.environ['FLICKR_KEY']
flickr = flickrapi.FlickrAPI(API_KEY, store_token=False)
LICENSES = {
        "1": {
            "name": "CC BY NC SA",
            "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
            },
        "2": {
            "name": "CC BY NC",
            "url": "http://creativecommons.org/licenses/by-nc/2.0/"
            },
        "3": {
            "name": "CC NC ND",
            "url": "http://creativecommons.org/licenses/by-nc-nd/2.0/"
            },
        "4": {
            "name": "CC BY",
            "url": "http://creativecommons.org/licenses/by/2.0/"
            },
        "5": {
            "name": "CC BY SA",
            "url": "http://creativecommons.org/licenses/by-sa/2.0/"
            },
        "6": {
            "name": "CC BY ND",
            "url": "http://creativecommons.org/licenses/by-nd/2.0/"
            },
        "7": 'public domain'
    }


class Photo:
    URL_TEMPLATE =  'http://farm1.staticflickr.com/{}/{}_{}_c.jpg'

    def __init__(self, photo_el):
        self.__photo_el = photo_el
        self.url = self.__url()
        self.url_original = self.__url_original()
        self.author = self.__author()
        self.license = self.__license()
        self.is_public_domain = self.__is_public_domain()

    def __url(self):
        server = self.__photo_el.attrib['server']
        photo_id = self.__photo_el.attrib['id']
        secret = self.__photo_el.attrib['secret']

        return self.URL_TEMPLATE.format(server, photo_id, secret)

    def __url_original(self):
        return self.__photo_el.find('urls').find('url').text

    def __author(self):
        return self.__photo_el.find('owner').attrib['username']

    def __license(self):
        return LICENSES[self.__photo_el.attrib['license']]

    def __is_public_domain(self):
        return True if self.__photo_el.attrib['license'] == '7' else False

def photos(city):
    FREE_LICENSES = '1,2,3,4,5,6,7,8'
    return flickr.photos_search(text=city, per_page='1', sort='interestingness-desc', license=FREE_LICENSES)

def fetch_first(set):
    first = set.find('photos').findall('photo')[0]
    return flickr.photos_getInfo(photo_id = first.attrib['id']).find('photo')

def location_photo(city):
    return Photo(fetch_first(photos(city)))
