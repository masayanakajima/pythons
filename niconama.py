#-*- coding:utf-8 -*-

import urllib2
import threading
from HTMLParser import HTMLParser
from urllib2 import build_opener,HTTPCookieProcessor
from urllib import urlencode#,parse_qs
from cookielib import CookieJar
from PyQt4 import QtGui
import codecs

class CommunityParser(HTMLParser):
	
	def __init__(self,txtname):
		HTMLParser.__init__(self)
		self.flag=False
		self.numOfCom=0
		self.numFlag=False
		self.next_url=""
		self.f = codecs.open("namelist/"+txtname+".txt","w","utf-8")

	def handle_starttag(self,tagname,attribute):
		if(tagname=="a" and len(attribute)>=2 and attribute[1][0]=="target" and attribute[1][1]=="_blank"):
			self.flag=True
		if(tagname=="a" and len(attribute)==2 and attribute[1][0]=="class" and attribute[1][1]=="next"):
			self.next_url =attribute[0][1]
		if(tagname=="strong" and self.numOfCom==0):
			self.numFlag=True

	def handle_data(self,data):
		if(self.flag):
		    if(data[0:1]!="\n" and data!=u"ゲスト" and data!=u"名無し"):
		    	self.f.write(data+"\n")
		    self.flag=False
		if(self.numFlag):
			self.numOfCom=int(data)
			self.numFlag=False

class CommunityAnalyzer:

	def __init__(self):
		self.addBar=ProgressBar()
		self.analyzeBar=ProgressBar()
		self.analyzeThread=AnalyzeThread(self.addBar)
		self.analyzeThread.setDaemon(True)

	def add_community(self,com_url,txtname):
		self.analyzeThread.set(com_url,txtname)
		self.analyzeThread.start()

	def get_intersection(self,txtname):
		if(len(txtname)==0):
			return []
		fst=txtname.pop()
		f=codecs.open("namelist/"+fst,"r","utf-8")
		lst=f.readlines()
		print(fst+":"+str(len(lst)))
		return self.get_commons(lst,self.get_intersection(txtname))
		
	def get_commons(self,lst1,lst2):
		if(len(lst2)==0):
			return lst1
		commons=[]
		for name1 in lst1:
			for name2 in lst2:
				if [name1]==[name2]:
					commons.append(name2)
					lst2.remove(name2)
					break

		return commons

	
class ProgressBar(QtGui.QProgressBar):

	def __init__(self):
		QtGui.QProgressBar.__init__(self)
		self.current=0
		self.setValue(0)

	def setMax(self,num):
		self.max=num
		self.current=0

	def update(self):
		self.current+=1
		if(self.current%10==0):
			self.setValue(float(self.current)/self.max*100)

	def finalize(self):
		self.setValue(100)


class AnalyzeThread(threading.Thread):

	def __init__(self,addBar):
		threading.Thread.__init__(self)
		self.opener = build_opener(HTTPCookieProcessor(CookieJar()))
		self.addBar=addBar
		self.login=False

	def set(self,com_url,txtname):
		self.txtname=txtname
		self.com_url=com_url

	def run(self):
		if not self.login:
			self.loging()

		response= self.opener.open(self.com_url)
		parser = CommunityParser(self.txtname)
		parser.feed(response.read().decode("utf-8"))
		self.addBar.setMax(float(parser.numOfCom)/30)
	
		while(True):
			if(parser.next_url!=""):
				response=self.open_url(parser.next_url)
				parser.next_url=""
				parser.feed(response.read().decode("utf-8"))
				self.addBar.update()
			else:
				self.addBar.finalize()
				break

		parser.f.close()

	def open_url(self,url):
		try:
			response=self.opener.open(url)
			return response
		except:
			return self.open_url(url)

	def loging(self):
		f = open("account.txt","r")
		account=f.read().split(",")
		post={"mail_tel":account[0],"password":account[1]}
		login_data = urlencode(post).encode("utf-8")
		self.opener.open("https://secure.nicovideo.jp/secure/login",login_data)			
		self.login=True