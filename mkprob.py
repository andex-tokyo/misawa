#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re

dict = {}
total = 0

for line in codecs.open("dogeza.txt.chasen","r","utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if lis[0] in dict:
            dict[lis[0]] += 1
        else:
            dict[lis[0]] = 1
        total += 1

fp = codecs.open("dogeza.prob", "w", "utf-8")

for x in dict.items():
    prob = x[1]/float(total)
    fp.write(x[0] + "\t" + str(prob) + "\n")

fp.close()

dict = {}
total = 0

for line in codecs.open("overseas.txt.chasen","r","utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if lis[0] in dict:
            dict[lis[0]] += 1
        else:
            dict[lis[0]] = 1
        total += 1

fp = codecs.open("overseas.prob", "w", "utf-8")

for x in dict.items():
    prob = x[1]/float(total)
    fp.write(x[0] + "\t" + str(prob) + "\n")

fp.close()

dict = {}
total = 0

for line in codecs.open("sleepy.txt.chasen","r","utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if lis[0] in dict:
            dict[lis[0]] += 1
        else:
            dict[lis[0]] = 1
        total += 1

fp = codecs.open("sleepy.prob", "w", "utf-8")

for x in dict.items():
    prob = x[1]/float(total)
    fp.write(x[0] + "\t" + str(prob) + "\n")

fp.close()

dict = {}
total = 0

for line in codecs.open("drummer.txt.chasen","r","utf-8"):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if lis[0] in dict:
            dict[lis[0]] += 1
        else:
            dict[lis[0]] = 1
        total += 1

fp = codecs.open("drummer.prob", "w", "utf-8")

for x in dict.items():
    prob = x[1]/float(total)
    fp.write(x[0] + "\t" + str(prob) + "\n")

fp.close()
