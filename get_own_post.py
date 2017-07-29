# Files and Functions are Imported
import requests
from constant import access_token ,base_url
import urllib

def get_own_post():
    # Function Logic to Download Own Most Recent Post..

    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (access_token)
    print 'GET request url : %s' %(request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code'] == 200:        #Download the post
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print "\n\t\t*****Your Recent image has been downloaded to C:\Users\Game Is Here\PycharmProjects\InstaBot*****"
        else:
            print '\n\t\t*****There Are No Post!*****'
    else:
        print '\n\t\t*****Status code other than 200 received!*****'