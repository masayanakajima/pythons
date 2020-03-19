import urllib.request,urllib.parse,urllib.error,re,time,warnings
from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor

BASE_URL = "https://account.nicovideo.jp/"

class LoginFailure(Exception):
	pass
class Nico:
	def __init__(self):
		self.opener = urllib.request.build_opener(HTTPCookieProcessor(CookieJar()))
	def login(self,htmldata,email,passwd):
		params = urllib.parse.urlencode({"mail_tel":email,"password":passwd,"next_url":"%2Fsearch%2F%25E3%2583%2597%25E3%2583%25AD%25E3%2582%25B0%25E3%2583%25A9%25E3%2583%259F%25E3%2583%25B3%25E3%2582%25B0%3Fmode%3Ds","site":"community"}).encode("utf-8")

		try:
			response=self.opener.open(htmldata.geturl(),params)
			driver=webdriver.Firefox()
			driver.get(response.geturl())
		except:
			print("url open error")
			raise LoginFailure

n=Nico()
url="https://account.nicovideo.jp/login"
htmldata = urllib.request.urlopen(url)
f = open("account.txt","r")
account=f.read().split(",")
n.login(htmldata,account[0],account[1])

f.close()