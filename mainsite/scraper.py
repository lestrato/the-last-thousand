from tweepy import Cursor, API, OAuthHandler, TweepError
from credentials import *

def fetch_twitter_posts(keyword, count):
    # Log into OAuth and set access with tokens
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

    # Construct the API instance
    api = API(auth)

    # Return a response and status based on the fetch
    response = None
    status = None

    try:
        response = []
        # Iterate through the first 'count' global tweets (pagination)
        for status in Cursor(api.search, q=keyword).items(count):
            new_post = {}
            new_post['text'] = status.text
            new_post['screen_name'] = status.user.screen_name
            new_post['name'] = status.user.name
            new_post['thumbnail'] = status.user.profile_image_url
            new_post['created_at'] = status.created_at
            new_post['favorite_count'] = status.favorite_count
            new_post['retweet_count'] = status.retweet_count
            new_post['id_str'] = status.id_str

            popularity = status.favorite_count + status.retweet_count
            response.append((popularity, new_post))

        # Sort based on sum of favourites + retweets; O(n log n)
        response.sort(reverse=True)
        # Get only the tweets now; O(n)
        response = [sublist[1] for sublist in response]

        status = 200 # Success!

    except TweepError as t:
        response = t.reason             # Error response description
        status = t.response.status_code # Error response code

    return response, status
