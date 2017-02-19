import os
import sys
from twython import Twython

#
# post a image twit with title
#
def twitter_post(consumer_key, consumer_secret, access_token_key, access_token_secret, title, description, siteurl, picture_path): 
    encoding = "utf-8"
    # message = title + " " + description + " " + siteurl
    # message = title + " @ http://julienleonard.com"

    twitter = Twython(app_key=consumer_key, app_secret=consumer_secret, oauth_token=access_token_key, oauth_token_secret=access_token_secret)

    image_open = open(picture_path, 'rb')
    image_ids = twitter.upload_media(media=image_open)
    result = twitter.update_status(status=message,media_ids=[image_ids['media_id']])
    image_open.close()
    return result


