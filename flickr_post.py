import sys
import flickrapi
import time
import xml.etree.ElementTree

#
# post an image into flickr with title, description and tags
#
def flickr_post( api_secret, api_key, title, description, tags, imagepath):
    result = ""
    flickr=flickrapi.FlickrAPI(api_key,api_secret)
    flickr.web_login_url("write")
    (token,frob)= flickr.get_token_part_one(perms='write')
    if not token: time.sleep(20)

    flickr.get_token_part_two((token, frob))
    result = flickr.upload(filename=imagepath, tags=tags, description=description, title=title)
    return result
    



