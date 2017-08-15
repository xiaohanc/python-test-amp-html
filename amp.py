import urllib
import string
content=urllib.urlopen('http://www.cnn.com/2017/08/15/politics/dreamhost-department-of-justice-trump-opponents/index.html').read()

'''get all html tags from the specific url and save it as a string'''

tags=content.split('>')

'''split the string by ">" and save it as a list'''



if tags[0]=="<!DOCTYPE html":
    print "1st pass"
tags1=tags[1].split(' ')
if tags1[0]=="<html" or tags1[0]=="<html amp":
    print "2nd pass"
if (string.find(content, "<head") != -1) and (string.find(content, "<body") != -1):
    print "3rd pass"
if (string.find(content, '<link rel="canonical" href="') != -1):
    print "4th pass"
if (string.find(content, '<meta charset="utf-8"') != -1):
    print "5th pass"
if (string.find(content, '<meta name="viewport"') != -1) and (string.find(content, 'content="width=device-width') != -1) and (string.find(content, 'minimum-scale=1') != -1):
    print "6th pass"
if '<script async src="https://cdn.ampproject.org/v0.js"' in tags:
    print "7th pass"
if (string.find(content, '<style amp-boilerplate') != -1) and (string.find(content, '<noscript ') != -1):
    print "8th pass"

'''check the format one by one according to each requirement'''




