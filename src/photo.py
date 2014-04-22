import os

import flickrapi

api_key = os.environ['FLICKR_KEY']
flickr = flickrapi.FlickrAPI(api_key, store_token=False)

def get_first(set):
    return set.find('photos').findall('photo')[0]

def url(photo):
    server = photo.attrib['server']
    photo_id = photo.attrib['id']
    secret = photo.attrib['secret']

    return 'http://farm1.staticflickr.com/{}/{}_{}_c.jpg'.format(server, photo_id, secret)

def location_photo(coordinates, city):

    lat, lng = coordinates.split(',')

    results = flickr.photos_search(lat=lat, lon=lng, radius='10', tag=city, per_page='1')
    photo = get_first(results)
    return url(photo)
