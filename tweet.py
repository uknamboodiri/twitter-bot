import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key='',
                           consumer_secret='')
auth.set_access_token('',
                      '')

api = tweepy.API(auth)

user = api.me()

# display a list of users who follow me @uknamboodiri
def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

# lets say you to mark some tweets as fav after search
search_text = 'python'
number_of_tweets = 2

for searched_tweet_result in tweepy.Cursor(api.search, search_text).items(number_of_tweets):
    try:
        searched_tweet_result.favorite()
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break

## print my followers
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)

# # displays whom the user follows names & other info
# # ----------------------------
user = api.get_user('<screen_name>')
for follower in user.friends():
    print(follower.name)

# displays home timeline
# ----------------------------
public_tweets = api.home_timeline()

for my_tweet in public_tweets:
    print(my_tweet.text)
