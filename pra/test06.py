from urllib.request import build_opener,HTTPCookieProcessor
from urllib.parse import urlencode,parse_qs
from http.cookiejar import CookieJar

opener = build_opener(HTTPCookieProcessor(CookieJar()))

encoding = "utf-8"
f = open("account.txt","r")
account=f.read().split(",")
post={"mail_tel":account[0],
	  "password":account[1]
}

data = urlencode(post).encode(encoding)

response = opener.open("https://secure.nicovideo.jp/secure/login",data)

response.close()

with opener.open("http://com.nicovideo.jp/search/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0?mode=s") as response:
	print(response.read().decode("utf-8"))