# Files and Functions are Imported
import requests
from constant import access_token ,base_url
from get_post_id import get_post_id
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
def delete_negative_comment(insta_username):
    # Function Logic to Delete Negative Comments..
    media_id = get_post_id(insta_username)
    request_url = ( + 'media/%s/comments/?access_token=%s') % (media_id, access_token)
    print 'GET request url : %s\n' % (request_url)
    comment_info = requests.get(request_url).json()

    def delete_negative_comment(insta_username):
        # Function Logic to Delete Negative Comments..
        media_id = get_post_id(insta_username)
        request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, access_token)
        print 'GET request url : %s\n' % (request_url)
        comment_info = requests.get(request_url).json()

        if comment_info['meta'][
            'code'] == 200:  # Check if there are Negative Comments Using textblob.sentiments Library
            if len(comment_info['data']):
                for x in range(0, len(comment_info['data'])):
                    comment_id = comment_info['data'][x]['id']
                    comment_text = comment_info['data'][x]['text']
                    blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                    if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                        print '\t(-)Negative comment : %s' % (comment_text)
                        delete_url = (base_url + 'media/%s/comments/%s/?access_token=%s') % (
                            media_id, comment_id, access_token)
                        print 'DELETE request url : %s' % (delete_url)
                        delete_info = requests.delete(delete_url).json()

                        if delete_info['meta']['code'] == 200:  # Check if negative comments are deleted or not
                            print '\t\t\t*****Comment successfully deleted!*****\n'
                        else:
                            print '\t\t\t*****Unable to delete comment!*****\n'
            else:
                print '\n\t\t\t*****There are no existing comments on the post!*****'
        else:  # if Page Not Found
            print '\n\t\t\t*****Status code other than 200 received!*****'

































