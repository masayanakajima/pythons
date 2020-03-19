# coding: UTF-8

import urllib.request
import http.client
import requests

url="http://www.google.com"
params={
	"foo":123,
}
'''
response=requests.get(url)
print(response.status_code)
print(response.text)
print(response.headers)
'''


req=urllib.request.Request(url)#"{}?{}".format(url,urllib.parse.urlencode(params)))
with urllib.request.urlopen(req) as res:
	body=res.read().decode("utf-8")
	print(body)
	header=res.getheaders()
	print(header)


'''
conn=http.client.HTTPConnection(url,80)
#conn.connect()
conn.request("GET","http://"+url)
res=conn.getresponse()
print(res.read().decode("utf-8"))
print(res.getheaders())
'''
