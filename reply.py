#!/usr/bin/python
# -*- coding:utf-8 -*-
from random import choice
import random
import os
import tweepy


consumer_key        = 'ATxOmrJgp3Dnhym0qVyou0v0j'
consumer_secret     = 'BgyiqwloODwFNP4qWEHTPzQzESXinUiJkEOkL2ozgEAHTjtXQJ'
access_token        = '929362088438390784-xVufp6rsXWCYhYGP7FEECmaSCKbZ7PK'
access_token_secret = 'bfEk1FZyBHhx6cWjzVOQSOFiIteCI2BkxQ3BoKXUzHYqW'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

misawa = []
for line in open('result.txt','r'):
  line = line.rstrip('\n')
  misawa.append(line)
text = random.choice(misawa)
text_list = text.split(',')
user_name = text_list[0]
status_id = text_list[1]
category = text_list[2] 

dir_path = './images_' + category + '/'
image_path = random.choice( os.listdir(dir_path) )
print(image_path)
print(user_name)
api.update_with_media(filename = dir_path + image_path,in_reply_to_status_id=status_id,status='@' + user_name)
