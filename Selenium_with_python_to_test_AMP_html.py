from selenium import webdriver
import urllib
import time

url = "C:\Cross Broswer Drivers\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(url)
driver.get("http://www.cnn.com/2017/08/15/politics/dreamhost-department-of-justice-trump-opponents/index.html")
'''using chrome webdriver of selenium to open the specified url'''

tags=urllib.urlopen('http://www.cnn.com/2017/08/15/politics/dreamhost-department-of-justice-trump-opponents/index.html').read().split('>')

'''get html tags from the specific url and save it as a list'''



if tags[0]=="<!DOCTYPE html":
    print 1
'''verify if the html starts with the doctype <!doctype html> or not'''

if driver.find_elements_by_tag_name("html") or driver.find_elements_by_tag_name("html amp"):
    print 2
if driver.find_elements_by_tag_name('body') and driver.find_elements_by_tag_name("head"):
    print 3
if driver.find_element_by_xpath("//link[@rel='canonical'][@href]"):
    print 4
if driver.find_element_by_xpath("//meta[@charset='utf-8']"):
    print 5
if driver.find_element_by_xpath("//meta[@name='viewport'][@content='width=device-width, initial-scale=1.0, minimum-scale=1.0']") or driver.find_element_by_xpath("//meta[@name='viewport'][@content='width=device-width, minimum-scale=1']"):
    print 6
if driver.find_element_by_xpath("//script[@src='https://cdn.ampproject.org/v0.js']"):
    print 7
if driver.find_element_by_xpath("//style[@amp-boilerplate]") and driver.find_element_by_xpath("//noscript/style/[@amp-boilerplate]"):
    print 8

'''using Xpath to locate each tags and attributes responding to its value, detect if each required format tags exists or not'''
