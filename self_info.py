import requests                     #fatch user data
from constant import access_token,base_url


def self_info():
  print "\t\t\tMY PROFILE\n"
  request_url = (base_url + 'users/self/?access_token=%s') % (access_token)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'User does not exist!'
  else:
    print 'Status code other than 200 received!'