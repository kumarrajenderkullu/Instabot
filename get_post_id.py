from get_user_id import get_user_id
from constant import base_url,access_token
import requests

def get_post_id(insta_username):
    # Function Logic to show the post id

    user_id = get_user_id(insta_username)   #Get the User's Id
    if user_id == None:
        print '\n\t\t*****User does not exist!*****'
        exit()
    request_url = (base_url + 'users/%s/media/recent/?access_token=%s') % (user_id, access_token)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print '\n\t\t*****There is no recent post of the user!*****'
            exit()
    else:
        print '\n\t\t*****Status code other than 200 received!*****'
        exit()