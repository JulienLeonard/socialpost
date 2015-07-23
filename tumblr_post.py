import time
import pytumblr
import sys

#
# post an image to tumblr with title, description, tags and link
#
def tumblr_image_post(oAuthConsumerKey, secretKey, tumblr3addr, tumblr4addr, blogurl, title, description, tags, imagefilepath, link):
    
    client = pytumblr.TumblrRestClient(oAuthConsumerKey, secretKey, tumblr3addr, tumblr4addr)

    result = client.create_photo(blogurl, state="publish", tags=tags.split(','), data=imagefilepath, caption=title + ":" + description, link=link)
    return result


