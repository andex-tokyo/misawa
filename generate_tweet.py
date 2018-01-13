#!/usr/bin/python # -*- coding: utf-8 -*- import sys
import tweepy
import codecs
import sys

consumer_key        = 'ATxOmrJgp3Dnhym0qVyou0v0j'
consumer_secret     = 'BgyiqwloODwFNP4qWEHTPzQzESXinUiJkEOkL2ozgEAHTjtXQJ'
access_token        = '929362088438390784-xVufp6rsXWCYhYGP7FEECmaSCKbZ7PK'
access_token_secret = 'bfEk1FZyBHhx6cWjzVOQSOFiIteCI2BkxQ3BoKXUzHYqW'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# このプログラムの使い方
# python generate_tweet.py 取得したいアカウント名 取得するツイート数 tweet.txt
user = sys.argv[1]
max_count = int(sys.argv[2])
outfile = sys.argv[3]

count = 200
total = 0
oldest = -1

fp = codecs.open(outfile,"w","utf-8")

tweets = api.user_timeline(count=count, screen_name=user)
if len(tweets) == 0:
    fp.close()
    sys.exit()

for tweet in tweets:
    tweet.text = tweet.text.replace("\n","")
    fp.write("%s,%d,%s\n" % (tweet.user.screen_name,tweet.id,tweet.text))
    total += 1
    oldest = tweet.id
    if total >= max_count:
        fp.close()
        sys.exit()

if oldest != -1:
    while True:
        tweets = api.user_timeline(count=count, screen_name=user, max_id=oldest-1)
        if len(tweets) == 0:
            break
        for tweet in tweets:
            tweet.text = tweet.text.replace("\n","")
            fp.write("%s,%d,%s\n" % (tweet.screen_name,tweet.id,tweet.text))
            total += 1
            oldest = tweet.id
            if total >= max_count:
                fp.close()
                sys.exit()

fp.close()
