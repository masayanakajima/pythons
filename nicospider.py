#-*- coding:utf-8 -*-

import urllib2
from HTMLParser import HTMLParser
from urllib2 import build_opener,HTTPCookieProcessor
from urllib import urlencode#,parse_qs
from cookielib import CookieJar

opener = build_opener(HTTPCookieProcessor(CookieJar()))

class CommunityParser(HTMLParser):
	
	def __init__(self):
		HTMLParser.__init__(self)
		self.strong_tag=False
		self.count=0
		self.sum=0
		self.member=0
		self.flag=False
	def handle_starttag(self,tagname,attribute):
		if tagname=="strong":
			self.count+=1
			self.strong_tag=True
	def handle_endtag(self,tag):
		if self.strong_tag:
			self.strong_tag=False
	def handle_data(self,data):
		if self.strong_tag:
			#print(data)
			if self.count==6:
				self.member=data
			if self.flag:
				if(data!=u"[動画関連情報]"):
					self.sum=data
				else:
					self.sum=-1
				self.flag=False
			if data==u"[生放送関連情報]":
				self.flag=True
			

class PageParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.communityParser=CommunityParser()
		self.communitypages=[]#list of url
		self.next_url=""

	def handle_starttag(self,tag,attribute):
		if(tag == "a" and attribute[0][0]=="href" and attribute[0][1][0:11]=="/community/"):
			self.communitypages.append(attribute[0][1])
		if(tag == "a" and attribute[0][0]=="href" and len(attribute)==2):
			if(attribute[1][1]=="next"):
				self.next_url=attribute[0][1]
	def handle_endtag(self,tagname):
		pass
	def handle_data(self,data):	
		pass

	def getData(self,community_page):
		self.communityParser.feed(community_page)
		factor=(self.communityParser.sum,self.communityParser.member)
		return factor

	def append_info(self,info_list):
		pages = set(self.communitypages)
		for url in pages:
			#print(url)
				response=urllib2.urlopen("http://com.nicovideo.jp"+url)
				info_list.append(self.getData(response.read().decode("utf-8")))
				self.communityParser = CommunityParser()
	def init(self):
		self.communitypages=[]
		response = opener.open(self.next_url)
		print(response.url)
		self.feed(response.read().decode("utf-8"))
		

if __name__=="__main__":
	info_list=[]
	parser = PageParser()
	
	encoding = "utf-8"
	f = open("account.txt","r")
	account=f.read().split(",")
	post={"mail_tel":account[0],
	      "password":account[1]
	}

	login_data = urlencode(post).encode(encoding)

	response = opener.open("https://secure.nicovideo.jp/secure/login",login_data)

	response.close()

	f2 = open("community.txt","w")
	f2.write("sum,member\n")

	response= opener.open("http://com.nicovideo.jp/search/%E3%82%B2%E3%83%BC%E3%83%A0%E5%AE%9F%E6%B3%81?mode=s&page=1&sort=u&order=d")
	parser.feed(response.read().decode("utf-8"))
		
	for i in range(0,40):
		parser.append_info(info_list)
		for e in info_list:
			if(e[0]!=-1):
				f2.write(e[0]+","+e[1]+"\n")
		info_list=[]
		parser.init()
		
	
	

	parser.communityParser.close()


