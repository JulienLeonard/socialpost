from utils import *
from wordpress_post import *
from twitter_post import *
from flickr_post import *
from tumblr_post import *
from pinterest_post import *
from facebook_post import *
from faa_post import *

#
# dispatch post per social network
# raise exception to inform superior process about result
#
def main():
    socialtype = sys.argv[1]

    if socialtype == "wordpress":
        status         = sys.argv[2]
        description    = sys.argv[3]
        title          = sys.argv[4]
        categories     = sys.argv[5]
        tags           = sys.argv[6]
        dropboxurl     = sys.argv[7]
        site           = sys.argv[8]
        bearer_key     = sys.argv[9]
        result = wordpress_post(status,description,title,categories,tags,dropboxurl,site,bearer_key)
        raise ValueError(result)
        
    if socialtype == "twitter":
        consumer_key        = sys.argv[2]
        consumer_secret     = sys.argv[3]
        access_token_key    = sys.argv[4]
        access_token_secret = sys.argv[5]
        title               = sys.argv[6]
        description         = sys.argv[7]
        siteurl             = sys.argv[8]
        picpath             = sys.argv[9]
        result = twitter_post(consumer_key, consumer_secret, access_token_key, access_token_secret, title, description, siteurl, picpath)
        if 'id_str' in result:        
            raise ValueError("postID : " + result['id_str'])

    if socialtype == "flickr":
        api_secret  = sys.argv[2]
        api_key     = sys.argv[3]
        title       = sys.argv[4]
        description = sys.argv[5]
        tags        = sys.argv[6]
        imagepath   = sys.argv[7]
        result = flickr_post( api_secret, api_key, title, description, tags, imagepath)
        raise ValueError(xml.etree.ElementTree.tostring(result))

    if socialtype == "tumblr":
        oAuthConsumerKey  = sys.argv[2]
        secretKey         = sys.argv[3]
        tumblr3addr       = sys.argv[4]
        tumblr4addr       = sys.argv[5]
        blogurl           = sys.argv[6]
        title             = sys.argv[7]
        description       = sys.argv[8]
        tags              = sys.argv[9]
        imagefilepath     = sys.argv[10]
        link              = sys.argv[11]
        result = tumblr_image_post(oAuthConsumerKey, secretKey, tumblr3addr, tumblr4addr, blogurl, title, description, tags, imagefilepath, link)
        if len(result) and 'id' in result:
            raise ValueError("id = " + str(result['id']))

    if socialtype == "pinterest":
        email    = sys.argv[2]
        password = sys.argv[3]
        pinboard = sys.argv[4]
        title    = sys.argv[5]
        wposturl = sys.argv[6]
        result = pinterest_post(email,password,pinboard,title,wposturl)
        return result
        
    if socialtype == "facebook":
        email     = sys.argv[2]
        password  = sys.argv[3]
        profileID = sys.argv[4]
        siteID    = sys.argv[5]
        title     = sys.argv[6]
        wposturl  = sys.argv[7]
        result = facebook_post(email,password,profileID,siteID,title,wposturl)
        return result

    if socialtype == "faa":
        username      = sys.argv[2]
        password      = sys.argv[3]
        userid        = sys.argv[4]
        title         = sys.argv[5]
        imagepathfile = sys.argv[6]
        description   = sys.argv[7]
        tags          = sys.argv[8]
        result = faa_post(username, password, userid, title, imagepathfile, description, tags)
        return result

if __name__ == '__main__':
  main()

