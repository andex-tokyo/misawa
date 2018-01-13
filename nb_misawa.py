#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import math
import os

drummer_dict = {}
overseas_dict = {}
sleepy_dict = {}
dogeza_dict = {}

for line in codecs.open("drummer.prob","r","utf-8"):
    line = line.rstrip()
    lis = line.split("\t")
    drummer_dict[lis[0]] = float(lis[1])

for line in codecs.open("overseas.prob","r","utf-8"):
    line = line.rstrip()
    lis = line.split("\t")
    overseas_dict[lis[0]] = float(lis[1])

for line in codecs.open("sleepy.prob","r","utf-8"):
    line = line.rstrip()
    lis = line.split("\t")
    sleepy_dict[lis[0]] = float(lis[1])

for line in codecs.open("dogeza.prob","r","utf-8"):
    line = line.rstrip()
    lis = line.split("\t")
    dogeza_dict[lis[0]] = float(lis[1])

drummer_prob = 0
overseas_prob = 0
sleepy_prob = 0
dogeza_prob = 0

os.system("./process_tweet.sh")
tweet_username = codecs.open("tweet_username.txt","r","utf-8")
tweet_id = codecs.open("tweet_id.txt","r","utf-8")
fp = codecs.open("result.txt", "w", "utf-8")

for line in codecs.open("tweet_text.txt.chasen","r","utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        misawa_type = max([drummer_prob, overseas_prob, sleepy_prob, dogeza_prob])
        result = ""
        if misawa_type == drummer_prob:
            result = "drummer"
        elif misawa_type == overseas_prob:
            result = "overseas"
        elif misawa_type == sleepy_prob:
            result = "sleepy"
        else:
            result = "dogeza"
        
        username = tweet_username.readline().replace('\n','')
        id = tweet_id.readline().replace('\n','')
        result = username + "," + id + "," + result + "\n"
        fp.write(result)

        drummer_prob = 0
        overseas_prob = 0
        sleepy_prob = 0
        dogeza_prob = 0

    else:
        lis = line.split("\t")
        if lis[0] in drummer_dict:
            drummer_prob += math.log(drummer_dict[lis[0]])
        else:
            drummer_prob += math.log(0.00001)

        if lis[0] in overseas_dict:
            overseas_prob += math.log(overseas_dict[lis[0]])
        else:
            overseas_prob += math.log(0.00001)

        if lis[0] in sleepy_dict:
            sleepy_prob += math.log(sleepy_dict[lis[0]])
        else:
            sleepy_prob += math.log(0.00001)

        if lis[0] in dogeza_dict:
            dogeza_prob += math.log(dogeza_dict[lis[0]])
        else:
            dogeza_prob += math.log(0.00001)

fp.close()
