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

def location_photo(city):

    results = flickr.photos_search(text=city, per_page='1', sort='interestingness-desc')
    photo = get_first(results)
    return url(photo)
