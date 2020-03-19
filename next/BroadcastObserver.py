from PyQt4 import QtCore,QtGui
import webbrowser
from HTMLParser import HTMLParser
import urllib2
from urllib2 import build_opener,HTTPCookieProcessor
from urllib import urlencode #parse_qs
from cookielib import CookieJar




class BroadcastObserver(QtCore.QObject,HTMLParser):
	
	def __init__(self,parent):
		super(BroadcastObserver,self).__init__()
		HTMLParser.__init__(self)
		self.timer=QtCore.QBasicTimer()
		self.curBroadcastURL=""
		self.communityPageURL=""
		self.bParser=BroadcastParser()

		self.opener = build_opener(HTTPCookieProcessor(CookieJar()))
		
		post={"mail_tel":"ma.cla.sora-40.2@ezweb.ne.jp",
		      "password":"M0rn1ng-1812"
		}

		login_data = urlencode(post).encode("utf-8")
		self.opener.open("https://secure.nicovideo.jp/secure/login",login_data)


	def receiveurl(self,url):
		self.curBroadcastURL=url
		self.changeFlag=False
		self.FirstFlag=True
		print("Input url is  "+self.curBroadcastURL)
		self.startObserver()

	def startObserver(self):
		bResponse=self.opener.open(self.curBroadcastURL)
		self.bParser.feed(bResponse.read().decode("utf-8"))
		self.timer.start(3000,self)

	def timerEvent(self,e):
		if self.changeFlag:
			webbrowser.open(self.curBroadcastURL)
			self.changeFlag=False
		cResponse=self.opener.open(self.bParser.communityURL)
		self.feed(cResponse.read().decode("utf-8"))

	def handle_starttag(self,tagname,attribute):
		if tagname=="a" and len(attribute)==2 and attribute[1][1]=="community":
			print(attribute[0][1])
			if self.curBroadcastURL !=attribute[0][1]:
				self.curBroadcastURL=attribute[0][1]
				if self.FirstFlag:
					self.FirstFlag=False
				else:
					self.changeFlag=True

	def handle_endtag(self,tag):
		if tag=="html":
			self.timer.start(3000,self)

class BroadcastParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.communityURL=""

	def handle_starttag(self,tagname,attribute):
		if tagname=="a" and len(attribute)==4 and attribute[2][1]=="commu_name":
			print(attribute[0][1])
			self.communityURL=attribute[0][1]
			

