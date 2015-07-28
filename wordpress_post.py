import os 
import time
from base64 import b64encode
import json
import requests
from wordpresspushmedia import *

#
# publish the image as a media in wordpress, and return the HTML to include into the post
#
def wordpress_publish_image(blogid,title,imageurl,bearer_key):
    url = "https://public-api.wordpress.com/rest/v1/sites/" + blogid + "/media/new"
    headers = {"Authorization": "bearer " + bearer_key }
    postdata = { 'media_urls' : [imageurl] }
    response = requests.post(url, data=json.dumps(postdata), headers=headers)
    jresponse = response.json()

    media = jresponse['media'][0];
    general_link = media['link'];
    linkdir = "/".join(general_link.split("/")[:-1])

    metadata = media['metadata'];
    if 'large' in metadata['sizes']:
        filebig = metadata['sizes']['large']['file'];
        src     = linkdir + "/" + filebig;
        width   = metadata['sizes']['large']['width'];
        height  = metadata['sizes']['large']['height'];
        sizetype = "size-large";
    else:
        src = media['link'];
        width   = metadata['width'];
        height  = metadata['height'];
        sizetype = "size-full";
    WPID    = media['id']

    SRC    = src;
    TITLE  = title;
    WIDTH  = str(width);
    HEIGHT = str(height);
    ID     = str(WPID);

    HTML = "<img src=\"" + SRC + "\" alt=\"" + TITLE + "\" width=\"" + WIDTH + "\" height=\"" + HEIGHT + "\" class=\"alignnone " + sizetype + " wp-image-" + ID + "\" />"
    return HTML

#
# post a wordpress post with image
#
def wordpress_post(status,description,title,categories,tags,imageurl,wordpress_blogid,wordpress_bearer_key):
    html = wordpress_publish_image(wordpress_blogid,title,imageurl, wordpress_bearer_key)
    content = html + "\n" + description
    headers = {"Authorization": "bearer " + wordpress_bearer_key }
    data = { 'content': content, "status":status, "title":title, "categories":categories, "tags":tags }
    try: 
        response = requests.post("https://public-api.wordpress.com/rest/v1/sites/" + wordpress_blogid + "/posts/new", data=data, headers=headers)
        result = response.json()
    except:
        print "wordpress post catch exception"
        result = ""
    return result
