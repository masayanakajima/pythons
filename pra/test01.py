#-*- coding:utf-8 -*-

import urllib.request,urllib.parse,urllib.error,re,time,warnings
from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor
from html.parser import HTMLParser

f=open("urltest.txt","w")
class CommunityParser(HTMLParser):
	
	def __init__(self):
		HTMLParser.__init__(self)
		self.link=False
	def handle_starttag(self,tagname,attribute):
		if tagname=="a" and attribute[0][0]=="href" :
			print(attribute[0][1])
			
	def handle_endtag(self,tag):
		#print("end:  "+tag)
		pass
	def handle_data(self,data):
		#print("data: "+data)
		pass
	
parser = CommunityParser()
url="http://com.nicovideo.jp/search/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0?mode=s"
htmldata = urllib.request.urlopen(url)
print(htmldata.read().decode("utf-8"))
print(htmldata.url)
f.close()
parser.close()
htmldata.close()