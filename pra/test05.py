#-*- coding:utf-8 -*-
import requests

with requests.Session() as c:
	url="https://account.nicovideo.jp/login"
	mail="mail"
	password="password"
	c.get(url)
	login_id =c.cookies['nicosid']
	ck=c.cookies
	login_data = dict(mail_tel=mail,password=password,auth_id=login_id,next_url="/")
	c.post(url,data=login_data,cookies=ck,headers={"Referer":"http://com.nicovideo.jp/search/"})
	page=c.get("http://com.nicovideo.jp/search/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0?mode=s")
	print(page.content.decode("utf-8"))